#!/usr/bin/env python3
"""Seeded adversarial finite diagnostics; no numerical output proves a theorem."""
from __future__ import annotations
import json, math, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigvalsh, eigh
ROOT=Path(__file__).resolve().parents[1];rng=np.random.default_rng(20260928);rows=[]
def unitary(d):
    q,r=np.linalg.qr(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))
    return q@np.diag(np.diag(r)/abs(np.diag(r)))
def H(psi,n):
    d=round(math.sqrt(psi.size));p=np.outer(psi,psi.conj())
    return sum(np.kron(np.eye(d**i),np.kron(p,np.eye(d**(n-2-i)))) for i in range(n-1))
def test(name,psi,n,bound,exact=None):
    h=H(psi,n);v=eigvalsh(h);pos=v[v>1e-9]
    assert len(pos) and v.min()>-1e-8
    gap=float(pos[0]); assert gap>=bound-2e-9
    if exact is not None:assert abs(gap-exact)<2e-9
    rows.append({'name':name,'N':n,'gap':gap,'lower_bound':bound,'nullity':int(sum(v<=1e-9)),
                 'exact_gap_target':exact})
e=np.eye(3,dtype=complex);u,w=e[:,0],e[:,1]
# Vary geometry, complex Schmidt unitary and common complex on-site basis.
for k in range(24):
    t=float(rng.uniform(0,.995));v=t*u+np.sqrt(1-t*t)*e[:,2];U=unitary(2)
    psi=sum(U[i,j]*np.kron([u,w][i],[w,v][j]) for i in range(2) for j in range(2))/np.sqrt(2)
    tau=abs(U[1,0])**2;delta=(2-t)*(1-t)/4;kappa=tau*delta/128
    Z=unitary(3);psi=np.kron(Z,Z)@psi
    # Check all complex contractions after the basis change.
    ww=Z@w;M=psi.reshape(3,3);ell=np.sqrt(2)*M@ww.conj();rr=np.sqrt(2)*M.T@ww.conj()
    amp=np.vdot(np.kron(ww,ww),psi)
    assert abs(abs(np.vdot(psi,np.kron(ell,ell)))-abs(amp))<2e-12
    assert abs(abs(np.vdot(psi,np.kron(rr,rr)))-abs(amp))<2e-12
    p=np.outer(psi,psi.conj());p1=np.kron(p,np.eye(9));p2=np.kron(np.eye(3),np.kron(p,np.eye(3)));p3=np.kron(np.eye(9),p)
    h=p1+p2+p3;g=h@h-(p1+p3)/2
    hv,hu=eigh(h);sel=hv>1e-9;T=hu[:,sel]/np.sqrt(hv[sel])[None,:]
    local_min=float(eigvalsh(T.conj().T@g@T)[0]);assert local_min>=kappa-1e-9
    for n in [3,4,5]:test('complex_flat_'+str(k),psi,n,1.5*kappa)
# Marker surface, coincident supports, near-critical supports.
for k in range(8):
    t=k/8;v=t*u+np.sqrt(1-t*t)*e[:,2];Z=unitary(3)
    psi=np.kron(Z,Z)@(np.kron(u,w)-np.exp(1j*k)*np.kron(w,v))/np.sqrt(2)
    for n in [3,4,5]:test('marker_'+str(k),psi,n,0,1-np.cos(np.pi/n))
for k in range(6):
    U=unitary(2);psi=np.zeros((3,3),complex);psi[:2,:2]=U/np.sqrt(2);Z=unitary(3)
    psi=np.kron(Z,Z)@psi.ravel()
    for n in [3,4,5]:test('common_support_'+str(k),psi,n,0,1-np.cos(np.pi/n))
# Whole fixed short-spectrum fibre and stronger certificate.
for theta in [0,.2,.6,1.,1.3,1.5,np.pi/2]:
    c,s=np.cos(theta),np.sin(theta);psi=np.zeros(9);psi[0]=c/np.sqrt(2);psi[1]=s/np.sqrt(2);psi[5]=-1/np.sqrt(2)
    for n in [3,4,5,6]:test('fibre_'+str(theta),psi,n,c*c/6)
    assert np.allclose(eigvalsh(H(psi,3)),[0]*21+[.5]+[1]*4+[1.5],atol=1e-10)
# d=4 disjoint supports, then an embedded genuinely three-dimensional marker.
e4=np.eye(4);psi=(np.kron(e4[:,0],e4[:,2])+np.kron(e4[:,1],e4[:,3]))/np.sqrt(2)
for n in [3,4]:test('d4_disjoint',psi,n,1,1)
psi=(np.kron(e4[:,0],e4[:,1])-np.kron(e4[:,1],e4[:,2]))/np.sqrt(2)
for n in [3,4]:test('d4_marker',psi,n,0,1-np.cos(np.pi/n))
report={'status':'PASS','full_Hamiltonian_cases':len(rows),'complex_four_site_cases':24,
        'seed':20260928,'zero_threshold':1e-9,'assertion_tolerance':2e-9,
        'scope':'Floating-point diagnostics only; not infinite-length or exact certificates.',
        'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'cases':rows}
(ROOT/'evidence'/'classification_numerics.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS:',len(rows),'full Hamiltonians, 24 complex four-site certificates')
