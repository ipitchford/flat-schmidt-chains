#!/usr/bin/env python3
"""Exact finite certificates for the accompanying qutrit-chain manuscript.

Only Python and SymPy are required. No numerical eigenvalue tolerance is used.
These checks verify finite identities, not a formalization of the analytic proofs.
Run from any directory: python code/verify_exact.py
"""
from __future__ import annotations
import json
import platform
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[dict] = []

def check(name: str, condition: bool, detail: object = None) -> None:
    if not bool(condition):
        raise AssertionError(name)
    item = {"name": name, "status": "PASS"}
    if detail is not None:
        item["detail"] = detail
    RESULTS.append(item)
    print("PASS", name, flush=True)

def projector(v: s.Matrix) -> s.Matrix:
    return v * v.conjugate().T / (v.conjugate().T * v)[0]

def ket(data: dict[tuple[int,int], object]) -> s.Matrix:
    v=s.zeros(9,1)
    for (i,j), value in data.items():
        v[3*i+j]=value
    return v

def hamiltonian(p: s.Matrix, n: int) -> s.Matrix:
    return sum((s.kronecker_product(s.eye(3**i), p, s.eye(3**(n-i-2)))
                for i in range(n-1)), s.zeros(3**n))

def charpoly(h: s.Matrix, x: s.Symbol) -> s.Expr:
    return s.factor(h.charpoly(x).as_expr())

def dimer_components(n: int) -> list[list[tuple[int,...]]]:
    unseen=set(product(range(3),repeat=n))
    out=[]
    while unseen:
        root=min(unseen); unseen.remove(root)
        stack=[root]; comp=[]
        while stack:
            word=stack.pop(); comp.append(word)
            for i in range(n-1):
                pair=word[i:i+2]
                if pair not in ((0,0),(1,2)):
                    continue
                other=(1,2) if pair==(0,0) else (0,0)
                w=word[:i]+other+word[i+2:]
                if w in unseen:
                    unseen.remove(w); stack.append(w)
        out.append(sorted(comp))
    return out

def block_for_words(h: s.Matrix, words: list[tuple[int,...]]) -> s.Matrix:
    ids=[sum(value*3**(len(w)-1-i) for i,value in enumerate(w)) for w in words]
    return h.extract(ids,ids)

x=s.symbols('x')
vd=ket({(0,0):1,(1,2):-1})
vm=ket({(0,1):1,(1,2):-1})
pd,pm=projector(vd),projector(vm)
for name,p in [('dimer',pd),('marker',pm)]:
    check(name+' projector', p*p==p and p.rank()==1)
    check(name+' H2 spectrum',charpoly(p,x)==x**8*(x-1))
    target=x**21*(x-1)**4*(2*x-1)*(2*x-3)/4
    check(name+' H3 spectrum', s.expand(charpoly(hamiltonian(p,3),x)-target)==0)

# The whole locally isospectral path: normalization and invariant singular values.
c,t=s.symbols('c t', real=True)
M=s.Matrix([[c,t,0],[0,0,-1],[0,0,0]])
# Actual coefficient matrix is M/sqrt(2), with c^2+t^2=1.
row_sq=s.expand(sum(v*v for v in (M*M)[0,:]))
check('isospectral-path contraction identity',
      s.rem(row_sq-1, s.Poly(c*c+t*t-1,c),c)==0,
      'M is unnormalized: (M^2)(M^2)^T has its only nonzero eigenvalue 1')
check('isospectral-path Schmidt identity',
      M*M.T==s.diag(c*c+t*t,1,0))

# Exhaustive direct-sum decomposition of the four-site dimer Hamiltonian.
expected_counts={2:{1:7,2:1},3:{1:16,2:4,3:1},4:{1:36,2:14,3:4,5:1}}
summary={}
H4=hamiltonian(pd,4)
for n in (2,3,4):
    h=hamiltonian(pd,n)
    comps=dimer_components(n)
    count=dict(sorted(Counter(map(len,comps)).items()))
    check(f'dimer N={n} component counts', count==expected_counts[n],count)
    seen_polys={}
    for comp in comps:
        k=len(comp); b=block_for_words(h,comp)
        poly=charpoly(b,x)
        seen_polys.setdefault(str(k),set()).add(str(poly))
        if k==1:
            check_cond=(b==s.zeros(1))
        elif k==2:
            check_cond=(s.expand(poly-x*(x-1))==0)
        elif k==3:
            check_cond=(s.expand(poly-x*(2*x-1)*(2*x-3)/4)==0)
        else:
            check_cond=(s.expand(poly-x*(x-1)*(4*x**3-16*x**2+18*x-5)/4)==0)
        if not check_cond:
            raise AssertionError(('unexpected component',n,comp,b,poly))
        ids={sum(value*3**(n-1-i) for i,value in enumerate(w)) for w in comp}
        for j in ids:
            for k2 in range(3**n):
                if k2 not in ids and h[j,k2]!=0:
                    raise AssertionError('component is not reducing')
    check(f'dimer N={n} all blocks reducing with stated spectra',True)
    summary[str(n)]={'component_counts':count,
                      'characteristic_polynomials':{k:sorted(v) for k,v in seen_polys.items()}}

words=[(0,0,0,0),(0,1,2,0),(1,2,0,0),(1,2,1,2),(0,0,1,2)]
K=s.Matrix([[3,-1,-1,0,-1],[-1,1,0,0,0],[-1,0,2,-1,0],
            [0,0,-1,2,-1],[-1,0,0,-1,2]])/2
check('five-state block from independent Kronecker Hamiltonian',K==block_for_words(H4,words))
B=K*K-s.Rational(2,5)*K
C=B[:4,:4]
L=s.Matrix([[1,0,0,0],[-s.Rational(1,3),1,0,0],
            [-s.Rational(7,16),-3,1,0],
            [s.Rational(5,24),5,-s.Rational(26,109),1]])
D=s.diag(s.Rational(12,5),s.Rational(1,30),s.Rational(109,320),s.Rational(78,545))
check('exact positive LDL certificate', C==L*D*L.T and all(D[i,i]>0 for i in range(4)))
T=s.eye(4).col_join(-s.ones(1,4))
check('five-state PSD certificate extension', B==T*C*T.T)
check('local rank maxima', [hamiltonian(pd,n).rank() for n in (2,3,4)]==[1,6,26])

# Stability arithmetic, including a genuinely full-Schmidt-rank example.
vstar=ket({(0,0):101,(1,2):-100,(2,1):1})
Cstar=s.Matrix(3,3,list(vstar))
Nstar=(vstar.T*vstar)[0]
fidelity=(vd.T*vstar)[0]**2/((vd.T*vd)[0]*Nstar)
eps2=1-fidelity
check('full-Schmidt-rank determinant', Cstar.det()==10100)
check('exact projector-distance squared', eps2==s.Rational(1,13468))
check('inside certified 1/90 ball',eps2<s.Rational(1,90)**2)
check('fails three-site overlap test',Cstar*Cstar==s.diag(10201,-100,-100)
      and s.Rational(10201,20202)>s.Rational(1,2))
check('uniform-gap radius arithmetic',s.Rational(1,10)-s.Rational(9,2)/90==s.Rational(1,20))

# Exact two-site hard-core block identities for the analytic dimer proof.
p=s.symbols('p',positive=True)
d=1-p
A=s.Matrix([[2*p,-p,-p],[-d,d,0],[-d,0,d]])
check('hard-core two-site generator spectrum',s.expand(charpoly(A,x)-x*(x-d)*(x-(1+p)))==0)
lam=s.symbols('lambda',positive=True)
coupling_cost=lam/((1+lam)*(1+2*lam))+2*lam**2/((1+lam)*(1+2*lam))
check('block boundary coupling cost',s.simplify(coupling_cost-lam/(1+lam))==0)

# Exact rank-two one-vacancy double-well certificates, for 50 sizes.
trial_records=[]
for ell in range(1,51):
    qs=[F(1,2)]*ell+[F(2)]*ell
    g=[F(1)]
    for q in qs: g.append(g[-1]*q)
    wl=sum(v*v for v in g[:ell]); wr=sum(v*v for v in g[ell:])
    f=[wr*v if j<ell else -wl*v for j,v in enumerate(g)]
    assert sum(a*b for a,b in zip(f,g))==0
    assert all(g[i+1]-q*g[i]==0 for i,q in enumerate(qs))
    energy=sum((f[i+1]-q*f[i])**2/(1+q*q) for i,q in enumerate(qs))
    norm=sum(v*v for v in f)
    rayleigh=energy/norm
    formula=F(4,5)*F(1,4)**ell*(1/wl+1/wr)
    upper=F(8,5)*F(1,4)**ell
    assert rayleigh==formula and rayleigh<=upper
    trial_records.append({'L':ell,'N':2*ell+1,'rayleigh':str(rayleigh),'upper_bound':str(upper)})
check('rank-two exact double-well trials',True,{'sizes':50,'N_min':3,'N_max':101})

# Rank-two overlap: exact symbolic Gram matrix confirms the stated norm.
a,b=s.symbols('a b',positive=True)
w1=ket({(1,0):1,(0,1):-a})/s.sqrt(1+a*a)
w2=ket({(2,0):1,(0,2):-b})/s.sqrt(1+b*b)
V=s.Matrix.hstack(s.kronecker_product(w1,s.eye(3)),s.kronecker_product(w2,s.eye(3)))
W=s.Matrix.hstack(s.kronecker_product(s.eye(3),w1),s.kronecker_product(s.eye(3),w2))
O=s.simplify(V.T*W)
# Ordering depends on vector convention: compare characteristic polynomials exactly.
vals=[a*a/(1+a*a)**2,a*a/(1+a*a)**2,b*b/(1+b*b)**2,b*b/(1+b*b)**2,
      a*a/((1+a*a)*(1+b*b)),b*b/((1+a*a)*(1+b*b))]
target=s.prod(x-v for v in vals)
check('rank-two overlap singular values',s.factor((O.T*O).charpoly(x).as_expr()-target)==0)

cert={'five_state_word_order':[''.join(map(str,w)) for w in words],
      'K':[[str(v) for v in row] for row in K.tolist()],
      'B_definition':'K^2 - (2/5) K',
      'L':[[str(v) for v in row] for row in L.tolist()],
      'D_diagonal':[str(D[i,i]) for i in range(4)],
      'PSD_extension':'T=[I_4; -1 -1 -1 -1], B=T L D L^T T^T',
      'local_decomposition':summary,
      'full_schmidt_rank_example':{'integer_coefficient_matrix':Cstar.tolist(),
                                  'normalization_squared':int(Nstar),
                                  'projector_distance_squared':str(eps2),
                                  'certified_uniform_gap':'1/20'},
      'rank_two_trials':trial_records}
# Convert SymPy integers in nested lists.
(ROOT/'evidence'/'finite_certificates.json').write_text(json.dumps(cert,indent=2,default=str)+'\n')
report={'status':'PASS','check_count':len(RESULTS),
        'python':platform.python_version(),'sympy':s.__version__,
        'scope':'Exact finite identities and certificates; analytic theorems are proved in paper, not formally verified.',
        'checks':RESULTS}
(ROOT/'evidence'/'exact_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'ALL {len(RESULTS)} EXACT CHECK GROUPS PASSED')
