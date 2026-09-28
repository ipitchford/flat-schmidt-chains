"""Reviewer-derived comparison with Bravyi--Gosset (2015), Theorem 1.
Exact algebra only. This does NOT claim that the explicit example was printed
in the 2015 paper. It verifies a corollary of its established classification.
"""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
x=S.symbols('x')
r2,r5=S.sqrt(2),S.sqrt(5)
vs={
 'gapless':S.Matrix([1/r2,S.Rational(1,2),-S.Rational(1,2),0]),
 'gapped':S.Matrix([S.Rational(1,2),(1+r5)/4,S.I*(r5-1)/4,0]),
}
rows=[]
def simp(m): return m.applyfunc(S.simplify)
target=S.expand(x**4*((x-1)**4-S.Rational(3,8)*(x-1)**2+S.Rational(1,256)))
for name,v in vs.items():
 assert S.simplify((v.conjugate().T*v)[0])==1
 M=S.Matrix(2,2,list(v))
 p=simp(v*v.conjugate().T)
 h=simp(S.kronecker_product(p,S.eye(2))+S.kronecker_product(S.eye(2),p))
 rho=simp(M*M.conjugate().T)
 O=simp(M.conjugate()*M)
 assert S.simplify(rho.det())==S.Rational(1,16)
 assert S.simplify(S.trace(O.conjugate().T*O))==S.Rational(3,8)
 assert S.simplify((O.conjugate().T*O).det())==S.Rational(1,256)
 # Direct characteristic polynomial, independent of the overlap inference.
 K=S.QQ.algebraic_field(r2) if name=='gapless' else S.QQ.algebraic_field(r5,S.I)
 dh=DomainMatrix.from_Matrix(h).convert_to(K)
 co=dh.charpoly()
 cp=S.Add(*[K.to_sympy(z)*x**(len(co)-i-1) for i,z in enumerate(co)])
 assert S.simplify(cp-target)==0
 T=S.Matrix([[S.conjugate(v[1]),S.conjugate(v[3])],[-S.conjugate(v[0]),-S.conjugate(v[2])]])
 abs2=[S.simplify(z*S.conjugate(z)) for z,multiplicity in T.eigenvals().items() for _ in range(multiplicity)]
 assert len(abs2)==2
 if name=='gapped': assert S.simplify(abs2[0]-abs2[1])!=0
 else: assert all(z==S.Rational(1,4) for z in abs2)
 rows.append({'label':name,'normalised_vector':[str(z) for z in v],
              'schmidt_probabilities':['(2+sqrt(3))/4','(2-sqrt(3))/4'],
              'overlap_singular_values':['(sqrt(2)+1)/4','(sqrt(2)-1)/4'],
              'H3_characteristic_polynomial':str(S.factor(cp)),
              'BG_transfer_eigenvalue_abs_squared':[str(z) for z in abs2]})
 print('PASS',name, 'H3=',S.factor(cp), 'T eigenvalue modulus squares=',abs2,flush=True)
report={'status':'PASS','scope':'Exact finite comparison; thermodynamic conclusions invoke BG Theorem 1, not numerical extrapolation.',
        'source':'https://arxiv.org/abs/1503.04035','states':rows,
        'qualification':'Does not duplicate the manuscripts flat Schmidt probabilities (1/2,1/2,0) or its exact three-site spectrum.'}
Path(__file__).with_name('qubit_comparison.json').write_text(json.dumps(report,indent=2)+'\n')
