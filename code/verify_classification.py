#!/usr/bin/env python3
"""Exact regression certificates for the new classification.
No floating-point predicates; these checks do not formalise the analytic proof.
"""
from __future__ import annotations
import json, platform, time
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence'; OUT.mkdir(exist_ok=True)
F=s.Rational; I=s.I; start=time.monotonic(); checks=[]; certs=[]
def check(name, condition, details=None):
    if not bool(condition): raise AssertionError(name)
    checks.append({'name':name,'status':'PASS','details':details})
    print('PASS',name,flush=True)
def zero(M): return all(s.simplify(x)==0 for x in M)
def kron(*args): return s.kronecker_product(*args)
e=[s.eye(3)[:,j] for j in range(3)]
def local(z):
    P=(z*z.H/2).applyfunc(s.expand)
    p=[kron(P,s.eye(9)),kron(s.eye(3),P,s.eye(3)),kron(s.eye(9),P)]
    h=sum(p,s.zeros(81)); g=h*h-(p[0]+p[2])/2
    return P,p,h,g

def positive_ldl(B):
    """Exact Hermitian LDL^*: rational Gaussian elimination, strictly positive pivots."""
    n=B.rows; L=s.eye(n); diag=[]
    for i in range(n):
        d=s.cancel(B[i,i]-sum(L[i,k]*s.conjugate(L[i,k])*diag[k] for k in range(i)))
        if d.is_positive is not True: raise AssertionError(('nonpositive pivot',i,d))
        diag.append(d)
        for j in range(i+1,n):
            L[j,i]=s.cancel((B[j,i]-sum(L[j,k]*s.conjugate(L[i,k])*diag[k] for k in range(i)))/d)
    # The recurrence is the exact factorisation; check independently by multiplication.
    check('LDL reconstruction '+str(len(certs)+1), zero(B-L*s.diag(*diag)*L.H))
    return [str(x) for x in diag]

# The exact three-dimensional fibre certificate.
x=s.Symbol('x');c=s.Symbol('c',real=True)
S=s.Matrix([[(1+c*c)/2,c*s.sqrt(2-c*c)/2,1/s.sqrt(2)],
            [c*s.sqrt(2-c*c)/2,(3-c*c)/2,0],[1/s.sqrt(2),0,1]])
check('fibre core characteristic polynomial',s.simplify(S.charpoly(x).as_expr()-(x*(x-F(3,2))**2-c*c/4))==0)
check('fibre core leading minors',s.simplify(S[:2,:2].det()-F(3,4))==0 and s.simplify(S.det()-c*c/4)==0)
check('quantitative constant 63+24sqrt5 < 128',63+24*s.sqrt(5)<128)
check('clipped two-bond minimum',s.Matrix([[F(1,2),-F(1,2)],[-F(1,2),1]]).eigenvals()=={(3-s.sqrt(5))/4:1,(3+s.sqrt(5))/4:1})
check('all chosen local constants below clipping threshold',F(1,9)<(3-s.sqrt(5))/4 and F(1,256)<(3-s.sqrt(5))/4)

# Count terms in zero-extended windows, independently of Hilbert-space size.
for n in range(2,31):
    diag=[0]*(n-1); pairs={}; hcount=[0]*(n-1)
    for j in range(-2,n-1):
        bonds=[i for i in range(j,j+3) if 0<=i<n-1]
        for i in bonds:
            hcount[i]+=1; diag[i]+=1
            if i in (j,j+2): diag[i]-=F(1,2)
        for a in bonds:
            for b in bonds:
                if a<b: pairs[a,b]=pairs.get((a,b),0)+1
    assert hcount==[3]*(n-1) and diag==[2]*(n-1)
    assert all(pairs.get((a,b),0)==(2 if b-a==1 else 1 if b-a==2 else 0)
               for a in range(n-1) for b in range(a+1,n-1))
check('clipped-window combinatorics N=2..30',True,{'sizes':29})

# General complex cases, with exact orthonormal Schmidt frames.
# z=sqrt(2)*psi, t=<u,v>; q gives a rational unitary.
for t,vt,aa,bb,phase in [
    (F(0),F(1),F(3,5),F(4,5),F(1)),
    (F(3,5),F(4,5),F(3,5),F(4,5),I),
    (F(5,13),F(12,13),F(5,13),F(12,13),(F(1))),
    (F(12,13),F(5,13),F(0),F(1),F(1))]:
    u,w=e[0],e[1]; v=t*e[0]+vt*e[2]
    a,b,cc,d=aa*phase,bb,-bb,aa*s.conjugate(phase)
    U=s.Matrix([[a,b],[cc,d]])
    z=(a*kron(u,w)+b*kron(u,v)+cc*kron(w,w)+d*kron(w,v)).applyfunc(s.expand)
    ell=a*u+cc*w; r=cc*w+d*v; psi=z/s.sqrt(2)
    check('unitarity and flat Schmidt '+str(t),zero(U.H*U-s.eye(2)) and s.simplify((z.H*z)[0]-2)==0)
    check('complex saturation contractions '+str(t),s.simplify((z.H*kron(ell,ell))[0]-cc)==0 and s.simplify((z.H*kron(r,r))[0]-cc)==0)
    P=(z*z.H/2).applyfunc(s.expand)
    p3a=kron(P,s.eye(3));p3b=kron(s.eye(3),P)
    xi=kron(psi,r)-kron(ell,psi)
    check('unit extremal pair mode '+str(t),s.simplify((xi.H*xi)[0]-1)==0 and zero((p3a+p3b)*xi-xi/2))
    tau=bb*bb; delta=(2-t)*(1-t)/4; kappa=tau*delta/128
    P,p,h,g=local(z)
    A=lambda p,q:(p+q)**2-(p+q)/2
    check('four-site positive-decomposition identity '+str(t),zero(g-A(p[0],p[1])-A(p[1],p[2])-2*p[0]*p[2]))
    C=s.Matrix.hstack(kron(z,s.eye(9)),kron(s.eye(3),z,s.eye(3)),kron(s.eye(9),z))
    columns=C.columnspace(); check('range rank '+str(t),len(columns)==26)
    T=s.Matrix.hstack(*columns)
    B=s.simplify(T.H*(g-kappa*h)*T)
    piv=positive_ldl(B)
    certs.append({'type':'general_flat','t':str(t),'tau':str(tau),'phase':str(phase),
                  'sqrt2_psi':[str(q) for q in z],'kappa':str(kappa),
                  'certificate':'T^*(G-kappa H)T=L diag(pivots)L^*, T exact independent range columns',
                  'dimension':26,'positive_LDL_pivots':piv})
    check('general flat four-site exact positivity '+str(t),True)

# Independently certify the stronger c^2/9 fibre bound with full 81-dimensional operators.
for cc,ss in [(F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))]:
    z=cc*kron(e[0],e[0])+ss*kron(e[0],e[1])-kron(e[1],e[2]);P,p,h,g=local(z)
    C=s.Matrix.hstack(kron(z,s.eye(9)),kron(s.eye(3),z,s.eye(3)),kron(s.eye(9),z))
    T=s.Matrix.hstack(*C.columnspace()); kappa=cc*cc/9
    piv=positive_ldl(s.simplify(T.H*(g-kappa*h)*T))
    certs.append({'type':'isospectral_fibre','c':str(cc),'s':str(ss),'kappa':str(kappa),
                  'dimension':26,'positive_LDL_pivots':piv})
    check('full-matrix sharp fibre certificate c='+str(cc),True)

# Exact check of the five-dimensional core construction at a rational point.
cc,ss=F(3,5),F(4,5);psi=(cc*kron(e[0],e[0])+ss*kron(e[0],e[1])-kron(e[1],e[2]))/s.sqrt(2)
r=s.Matrix([cc*cc,cc*ss,-ss]);ell=e[0]
alpha=cc/s.sqrt(2);beta=s.sqrt(1-cc*cc/2)
C=s.Matrix.hstack(kron(psi,s.eye(9)),kron(s.eye(3),psi,s.eye(3)),kron(s.eye(9),psi));K=s.simplify(C.H*C)
D=s.diag(*([F(1,2)]*9+[0]*9+[F(1,2)]*9))
a=kron(r,r);ap=(psi-alpha*a)/beta;b=kron(ell,r);dd=kron(ell,ell);dp=(psi-alpha*dd)/beta
Z=s.zeros(27,5);Z[:9,0]=a;Z[:9,1]=ap;Z[9:18,2]=b;Z[18:,3]=dd;Z[18:,4]=dp
check('core basis orthonormal',zero(Z.H*Z-s.eye(5)))
T=s.Matrix([[1/s.sqrt(2),0,0],[0,1/s.sqrt(2),0],[0,0,1],[1/s.sqrt(2),0,0],[0,1/s.sqrt(2),0]])
check('even core equals displayed S',zero(T.H*Z.H*(K-D)*Z*T-S.subs(c,cc)))
check('five-dimensional core reducing',zero((K-D)*Z-Z*(Z.H*(K-D)*Z)))

report={'status':'PASS','check_groups':len(checks),'exact_PSD_certificates':len(certs),
        'elapsed_seconds':time.monotonic()-start,'python':platform.python_version(),'sympy':s.__version__,
        'scope':'Exact finite regression certificates; general theorems remain analytic proofs, not proof-assistant verified.',
        'checks':checks}
(OUT/'classification_exact.json').write_text(json.dumps(report,indent=2)+'\n')
(OUT/'classification_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
print('ALL',len(checks),'EXACT CHECK GROUPS PASSED',flush=True)
