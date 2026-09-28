#!/usr/bin/env python3
"""Verify the frozen release and both supplied archive manifests, without writes."""
from __future__ import annotations
import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def verify(folder: Path) -> int:
    manifest=folder/'MANIFEST.sha256'
    if not manifest.is_file():
        raise FileNotFoundError(manifest)
    count=0
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        expected, name=line.split(None,1)
        name=name.lstrip('* ')
        target=(folder/name).resolve()
        if not target.is_relative_to(folder.resolve()):
            raise ValueError(f'Unsafe manifest path: {name}')
        actual=hashlib.sha256(target.read_bytes()).hexdigest()
        if actual!=expected:
            raise ValueError(f'Hash mismatch: {target}')
        count+=1
    print(f'PASS: {count} hashes in {folder.relative_to(ROOT) if folder!=ROOT else "."}')
    return count
if __name__=='__main__':
    verify(ROOT)
    verify(ROOT/'evidence/baseline_v0_1')
    verify(ROOT/'review/supplied_referee_checks')
