"""Reviewer-built checks, not imported from the submitted package.
Finite numerical tests are diagnostics, not proofs of infinite-volume claims.
"""
from __future__ import annotations
import itertools, json, math, platform
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigvalsh

OUT=Path(__file__).parent

def local_projector(terms: dict[tuple[int,int],complex]) -> np.ndarray:
    v=np.zeros(9,dtype=complex)
    for (a,b),z in terms.items(): v[3*a+b]=z
    v/=np.linalg.norm(v)
    return np.outer(v,v.conj())

def assemble_by_words(p: np.ndarray,n:int) -> np.ndarray:
    """Act on each word and each bond directly; no Kronecker construction."""
    words=list(itertools.product(range(3),repeat=n))
    index={w:i for i,w in enumerate(words)}
    h=np.zeros((3**n,3**n),complex)
    nz=[[(divmod(j,3),p[j,k]) for j in range(9) if p[j,k]!=0] for k in range(9)]
    for col,w in enumerate(words):
        for b in range(n-1):
            for (u,v),z in nz[3*w[b]+w[b+1]]:
                row=index[w[:b]+(u,v)+w[b+2:]]
                h[row,col]+=z
    assert np.max(np.abs(h-h.conj().T))<1e-12
    return h

def positive_gap(h:np.ndarray)->tuple[float,int]:
    vals=eigvalsh(h,check_finite=True)
    assert vals[0]>-1e-9
    pos=vals[vals>1e-9]
    assert pos.size
    return float(pos[0]),int(np.sum(vals<=1e-9))

pd=local_projector({(0,0):1,(1,2):-1})
models={'dimer':pd,'marker':local_projector({(0,1):1,(1,2):-1}),
        'opposing':local_projector({(1,0):2,(0,1):-1})+local_projector({(2,0):1,(0,2):-2}),
        'star':local_projector({(0,0):101,(1,2):-100,(2,1):1})}
rows=[]
for name,p in models.items():
    for n in range(2,7):
        gap,nullity=positive_gap(assemble_by_words(p,n))
        if name=='dimer': assert gap>=.25-1e-10
        if name=='marker': assert abs(gap-(1-math.cos(math.pi/n)))<1e-10
        if name=='star': assert gap>=.05-1e-10
        if name=='opposing' and n%2==1:
            assert gap<=1.6*4**(-(n-1)//2)+1e-10
        rows.append({'model':name,'n':n,'gap':gap,'nullity':nullity})

# Complex perturbations at exactly specified projective distance sin(theta).
rng=np.random.default_rng(9282026)
v=np.zeros(9,complex);v[0]=1/math.sqrt(2);v[5]=-1/math.sqrt(2)
pert=[]
for j in range(6):
    z=rng.normal(size=9)+1j*rng.normal(size=9)
    z-=v*np.vdot(v,z);z/=np.linalg.norm(z)
    eps=.01
    w=math.sqrt(1-eps**2)*v+eps*z
    q=np.outer(w,w.conj())
    measured=float(np.linalg.norm(q-pd,2))
    assert abs(measured-eps)<1e-12
    for n,expected_null in ((2,8),(3,21),(4,55)):
        gap,nullity=positive_gap(assemble_by_words(q,n))
        assert nullity==expected_null
        baseline={2:1,3:.5,4:.4}[n]
        assert gap>=baseline-(n-1)*eps-1e-10
        pert.append({'sample':j,'n':n,'projector_distance':measured,'gap':gap,'nullity':nullity})

# Hard-core heat bath: direct weighted configuration graph, symmetric transform.
hc=[]
for m in range(1,11):
    states=[s for s in range(1<<m) if not(s & (s<<1))]
    index={s:i for i,s in enumerate(states)}
    for lam in (.01,.1,1.,10.,100.):
        p,d=lam/(1+lam),1/(1+lam)
        h=np.zeros((len(states),len(states)))
        for i,s in enumerate(states):
            for bit in range(m):
                target=s^(1<<bit)
                if target not in index:continue
                j=index[target]
                rate=d if s&(1<<bit) else p
                h[i,i]+=rate
                h[i,j]=-math.sqrt(p*d)
        vals=eigvalsh(h)
        assert abs(vals[0])<1e-10
        gap=float(vals[1]); lower=d*d
        assert gap>=lower-1e-10
        hc.append({'m':m,'activity':lam,'gap':gap,'claimed_lower_bound':lower})

# Exact arithmetic for arbitrary opposing biases and sector cuts.
trials=[]
for a,b in ((F(1,2),F(2)),(F(2,3),F(3,2)),(F(1,3),F(2)),(F(3,4),F(5,4))):
    A,B=-math.log(float(a)),math.log(float(b))
    for n in (5,8,13,21,34,55):
        m=n-1;k=math.ceil(m*B/(A+B))
        assert 1<=k<m
        qs=[a]*k+[b]*(m-k)
        g=[F(1)]
        for q in qs:g.append(g[-1]*q)
        wl=sum(t*t for t in g[:k]);wr=sum(t*t for t in g[k:])
        f=[wr*t for t in g[:k]]+[-wl*t for t in g[k:]]
        assert sum(t*u for t,u in zip(f,g))==0
        energy=sum((f[i+1]-q*f[i])**2/(1+q*q) for i,q in enumerate(qs))
        rq=energy/sum(t*t for t in f)
        predicted=a**(2*k)/(1+a*a)*(1/wl+1/wr)
        assert rq==predicted
        assert F(1)<=wl and (a/b)**2<=wr
        assert a/b<=g[-1]<=1
        constant=(1+(b/a)**2)/(1+a*a)
        bound=float(constant)*math.exp(-2*A*B/(A+B)*m)
        assert float(rq)<=bound*(1+1e-12)
        trials.append({'a':str(a),'b':str(b),'n':n,'cut':k,'exact_rayleigh_quotient':str(rq),
                       'rayleigh_float':float(rq),'analytic_exponential_bound_float':bound})

report={'status':'PASS','scope':'Independent finite diagnostics, not asymptotic proof or full classification.',
 'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
 'tolerances':{'positive_eigenvalue':1e-9,'gap_checks':1e-10},
 'direct_full_hamiltonians':rows,'complex_rank_one_perturbations':pert,
 'hard_core_heatbath':hc,'exact_opposing_bias_trials':trials}
(OUT/'independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: 20 full Hamiltonians, 18 complex-perturbation chains, 50 hard-core systems, 24 exact Rayleigh trials.')
print(json.dumps(report['environment']))
