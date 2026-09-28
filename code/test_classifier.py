#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import sympy as s
from classify_flat import classify_flat
ROOT=Path(__file__).resolve().parents[1];rows=[]
r2=s.sqrt(2);I=s.I;F=s.Rational
cases=[('qubit_phi',s.eye(2)/r2,'gapless'),
       ('qubit_twist',s.Matrix([[F(3,5),4*I/5],[4*I/5,F(3,5)]])/r2,'gapless'),
       ('dimer',s.Matrix([[1,0,0],[0,0,-1],[0,0,0]])/r2,'uniformly_gapped'),
       ('marker',s.Matrix([[0,1,0],[0,0,-1],[0,0,0]])/r2,'gapless'),
       ('interior',s.Matrix([[F(3,5),F(4,5),0],[0,0,-1],[0,0,0]])/r2,'uniformly_gapped'),
       ('common_support',s.diag(1,I,0)/r2,'gapless'),
       ('d4_disjoint',s.Matrix([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])/r2,'uniformly_gapped')]
# Exact non-real on-site rotation, preserving support invariants.
Z=s.Matrix([[F(3,5),4*I/5,0],[4*I/5,F(3,5),0],[0,0,I]])
for name,M,expected in list(cases):
    if M.rows==3: cases.append(('rotated_'+name,(Z*M*Z.T).applyfunc(s.simplify),expected))
for name,M,expected in cases:
    out=classify_flat(M)
    if out['classification']!=expected: raise AssertionError(name)
    rows.append({'name':name,'result':{k:str(v) for k,v in out.items()}})
# Reject inputs that could invite false exact-zero conclusions.
reject=[s.Matrix([[1.,0.],[0.,1.]])/r2,s.Matrix([[1,0],[0,0]]),s.Matrix([[2,0],[0,1]])/s.sqrt(5)]
for j,M in enumerate(reject):
    try:classify_flat(M)
    except ValueError as e:rows.append({'name':'rejection_'+str(j),'message':str(e)})
    else:raise AssertionError('Out-of-scope input accepted')
# The normal-word recurrence, by direct enumeration independently of the formula.
import itertools
D=[1,3]
for n in range(2,9):D.append(3*D[-1]-D[-2])
for n in range(9):
    actual=sum(all(w[i:i+2]!=(1,2) for i in range(n-1)) for w in itertools.product(range(3),repeat=n))
    if actual!=D[n]: raise AssertionError(('normal words',n))
# Reviewer regression: generic symbolic rank must never imply a uniform phase.
x=s.Symbol('x',real=True)
family=s.Matrix([[(1-x*x)/(1+x*x),0,2*x/(1+x*x)], [0,-1,0], [0,0,0]])/r2
try: classify_flat(family)
except ValueError as exc:
    if 'Free symbols' not in str(exc): raise AssertionError('Wrong symbolic rejection')
else: raise AssertionError('Unspecialised family accepted')
for value,expected,dimension in [(0,'gapless',2),(1,'uniformly_gapped',1)]:
    result=classify_flat(family.subs(x,value))
    if result['classification']!=expected or result['intersection_dimension']!=dimension:
        raise AssertionError(('specialisation',value,result))
    rows.append({'name':'review_specialisation_'+str(value),'result':{k:str(v) for k,v in result.items()}})
report={'status':'PASS','classifier_cases':len(cases),'input_rejections':3,
        'review_regressions':3,'normal_word_counts_N0_to_8':D,'cases':rows}
(ROOT/'evidence'/'classifier_tests.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS:',len(cases),'exact classifier cases, 3 input rejections, normal words N=0..8')
