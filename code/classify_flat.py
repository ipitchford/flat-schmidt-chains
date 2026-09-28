#!/usr/bin/env python3
"""Exact-input classifier for the manuscript's flat Schmidt-rank-two class.
The input is the coefficient matrix M of a NORMALISED forbidden vector.
Floating inputs are rejected: numerical equality is not a phase certificate.
Free symbols are rejected: specialise parameter families before classification.
"""
from __future__ import annotations
import sympy as s

def classify_flat(M: s.MatrixBase) -> dict:
    M=s.Matrix(M)
    if M.rows!=M.cols or M.rows<2: raise ValueError('Expected a square on-site coefficient matrix, d>=2.')
    if any(z.has(s.Float) for z in M): raise ValueError('Use exact algebraic entries, not floating-point approximations.')
    if M.free_symbols:
        raise ValueError('Free symbols are not supported; specialise parameters to exact constants before classification.')
    simple=lambda A:A.applyfunc(s.simplify)
    iszero=lambda A:all(s.simplify(z)==0 for z in A)
    if s.simplify(s.trace(M*M.H)-1)!=0: raise ValueError('The forbidden vector must be exactly normalised.')
    PL=simple(2*M*M.H); PR=simple(2*M.T*M.conjugate())
    if not (M.rank()==2 and iszero(PL*PL-PL) and iszero(PR*PR-PR)):
        raise ValueError('This classifier covers exactly two equal nonzero Schmidt probabilities.')
    A=s.Matrix.hstack(*PL.columnspace());B=s.Matrix.hstack(*PR.columnspace())
    ker=s.Matrix.hstack(A,-B).nullspace()
    dim=len(ker)
    result={'local_dimension':M.rows,'intersection_dimension':dim,
            'scope':'open chains, no boundary terms, normalised rank-one projector'}
    if dim==2:
        return result|{'classification':'gapless','exact_gap':'1-cos(pi/N)','reason':'coincident Schmidt supports'}
    if dim==0:
        return result|{'classification':'uniformly_gapped','lower_bound':'1-||Pi_L Pi_R|| > 0',
                      'reason':'disjoint Schmidt supports'}
    z=simple(A*ker[0][:2,0]);z2=s.simplify((z.H*z)[0])
    amp=s.simplify((z.conjugate().T*M*z.conjugate())[0])
    tau=s.simplify(2*amp*s.conjugate(amp)/(z2*z2))
    t2=s.simplify(s.trace(PL*PR)-1)
    result|={'tau':tau,'t_squared':t2,'intersection_vector_unnormalised':z}
    if tau==0:
        return result|{'classification':'gapless','exact_gap':'1-cos(pi/N)','reason':'balanced marker'}
    if tau.is_positive is not True:
        raise ValueError('Symbolic positivity of tau was not resolved; specialise the exact input.')
    bound=s.simplify(3*tau*(2-s.sqrt(t2))*(1-s.sqrt(t2))/1024)
    return result|{'classification':'uniformly_gapped','lower_bound':bound,'reason':'four-site saturation obstruction'}

if __name__=='__main__':
    for name,z in [('dimer',s.Matrix([[1,0,0],[0,0,-1],[0,0,0]])),
                   ('marker',s.Matrix([[0,1,0],[0,0,-1],[0,0,0]])),
                   ('interior',s.Matrix([[s.Rational(3,5),s.Rational(4,5),0],[0,0,-1],[0,0,0]]))]:
        print(name,classify_flat(z/s.sqrt(2)))
