#!/usr/bin/env python3
"""Standard-library exhaustive diagnostic of the dimer-sector decomposition.
Checks every computational word through length eight. This finite enumeration
supports, but does not replace, the arbitrary-length proof in Section 4.
"""
from __future__ import annotations
import json
from collections import defaultdict
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def frozen(w):
    return tuple((i,s) for i,s in enumerate(w)
                 if (s==1 and (i+1==len(w) or w[i+1]!=2))
                 or (s==2 and (i==0 or w[i-1]!=1)))

def tilings(length):
    a,b=1,1
    for _ in range(length): a,b=b,a+b
    return a

rows=[]
for n in range(1,9):
    groups=defaultdict(set)
    for w in product(range(3),repeat=n): groups[frozen(w)].add(w)
    for key,group in groups.items():
        positions=[-1]+[i for i,_ in key]+[n]
        expected=1
        for l,r in zip(positions,positions[1:]): expected*=tilings(r-l-1)
        assert len(group)==expected,(n,key,len(group),expected)
        seen={min(group)}; stack=list(seen)
        while stack:
            w=stack.pop()
            for i in range(n-1):
                pair=w[i:i+2]
                if pair in ((0,0),(1,2)):
                    v=w[:i]+((1,2) if pair==(0,0) else (0,0))+w[i+2:]
                    assert frozen(v)==key
                    if v not in seen: seen.add(v);stack.append(v)
        assert seen==group
    rows.append({'N':n,'words':3**n,'components':len(groups),'status':'PASS'})
    print('PASS',rows[-1])
report={'status':'PASS','scope':'Exhaustive finite sector diagnostic, not a proof for unbounded N',
        'total_words':sum(r['words'] for r in rows),'cases':rows}
(ROOT/'evidence'/'sector_structure_checks.json').write_text(json.dumps(report,indent=2)+'\n')
