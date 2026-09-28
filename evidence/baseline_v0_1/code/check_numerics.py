#!/usr/bin/env python3
"""Floating-point regression checks. These are NOT proof certificates.
Uses a separately implemented tensor construction and Hermitian eigensolver.
Set OPENBLAS_NUM_THREADS=1 before running; use --max-n 6 for default checks.
"""
from __future__ import annotations
import argparse
import csv
import json
import platform
from pathlib import Path
import numpy as np
import scipy
import scipy.linalg as la
import scipy.sparse as sp

ROOT=Path(__file__).resolve().parents[1]

def vec(items):
    v=np.zeros(9,dtype=complex)
    for (i,j),z in items.items(): v[3*i+j]=z
    return v/la.norm(v)

def proj(v):
    return np.outer(v,v.conjugate())

def hamiltonian(p,n):
    out=sp.csr_matrix((3**n,3**n),dtype=complex)
    for i in range(n-1):
        out+=sp.kron(sp.kron(sp.eye(3**i),sp.csr_matrix(p)),sp.eye(3**(n-i-2)),format='csr')
    return out.toarray()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-n',type=int,default=6)
    args=ap.parse_args()
    if not 4<=args.max_n<=8:
        ap.error('--max-n must be between 4 and 8 (dense eigenvalue computation)')
    u=np.array([1,0,0],dtype=complex)
    w=np.array([0,1,0],dtype=complex)
    v=np.array([3/5,0,4j/5],dtype=complex)
    complex_marker=(3*np.kron(u,w)-4*np.kron(w,v))/5
    models={
      'marker_balanced':(proj(vec({(0,1):1,(1,2):-1})),lambda n:1-np.cos(np.pi/n),'equality'),
      'marker_complex_biased':(proj(complex_marker),lambda n:1-(24/25)*np.cos(np.pi/n),'equality'),
      'dimer_balanced':(proj(vec({(0,0):1,(1,2):-1})),lambda n:1/4,'lower'),
      'dimer_biased_3_4':(proj(vec({(0,0):3,(1,2):-4})),lambda n:(16/25)**2,'lower'),
      'full_schmidt_rank_star':(proj(vec({(0,0):101,(1,2):-100,(2,1):1})),lambda n:1/20,'lower'),
      'rank_two_opposing':(proj(vec({(1,0):2,(0,1):-1}))+proj(vec({(2,0):1,(0,2):-2})),
                           lambda n:(8/5)*4**(-(n-1)/2) if n%2==1 else float('nan'),'upper_odd'),
      'rank_two_equal_bias':(proj(vec({(1,0):1,(0,1):-2}))+proj(vec({(2,0):1,(0,2):-2})),
                             lambda n:1-(4/5)*np.cos(np.pi/n),'equality'),
    }
    rows=[]
    for name,(p,bound,kind) in models.items():
        assert la.norm(p@p-p)<1e-12
        for n in range(2,args.max_n+1):
            h=hamiltonian(p,n)
            eig=la.eigvalsh(h,check_finite=False)
            positive=eig[eig>1e-9]
            gap=float(positive[0]); target=float(bound(n))
            if kind=='equality': assert abs(gap-target)<1e-8,(name,n,gap,target)
            elif kind=='lower': assert gap+1e-8>=target,(name,n,gap,target)
            elif n%2==1: assert gap<=target+1e-8,(name,n,gap,target)
            row={'model':name,'N':n,'dimension':3**n,'nullity_numeric':int(np.sum(abs(eig)<1e-9)),
                 'gap_numeric':gap,'comparison_value':target,'comparison':kind,
                 'min_eigenvalue_numeric':float(eig[0])}
            rows.append(row)
            print(name,n,f'{gap:.14g}',flush=True)
    with (ROOT/'evidence'/'numerical_regression.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    summary={'status':'PASS','cases':len(rows),'max_n':args.max_n,'zero_threshold':1e-9,
             'bound_tolerance':1e-8,'python':platform.python_version(),'numpy':np.__version__,
             'scipy':scipy.__version__,'scope':'Floating-point sanity checks only; no proof is inferred from finite-size scaling.'}
    (ROOT/'evidence'/'numerical_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('ALL',len(rows),'NUMERICAL REGRESSION CASES PASSED')

if __name__=='__main__': main()
