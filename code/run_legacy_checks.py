#!/usr/bin/env python3
"""Rerun baseline and supplied-referee programmes without changing their archives."""
from __future__ import annotations
import hashlib,json,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'evidence'/'reruns';OUT.mkdir(exist_ok=True)
records=[];env=os.environ|{'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONHASHSEED':'0'}
def run(script, dest):
    start=time.monotonic();p=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,env=env,timeout=180)
    (dest/(script.stem+'_run.txt')).write_text(p.stdout+p.stderr)
    records.append({'programme':script.name,'source_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
                    'returncode':p.returncode,'PYTHONHASHSEED':env['PYTHONHASHSEED'],'elapsed_seconds':time.monotonic()-start})
    if p.returncode:raise RuntimeError(p.stdout+p.stderr)
    print('PASS',script.name,flush=True)
with tempfile.TemporaryDirectory(prefix='qutrit-rerun-') as tmp:
    tmp=Path(tmp);base=tmp/'baseline';(base/'code').mkdir(parents=True);(base/'evidence').mkdir()
    dest=OUT/'baseline';dest.mkdir(exist_ok=True)
    for source in sorted((ROOT/'evidence/baseline_v0_1/code').glob('*.py')):
        script=base/'code'/source.name;shutil.copy2(source,script);run(script,dest)
    for f in (base/'evidence').glob('*'):shutil.copy2(f,dest/f.name)
    ref=tmp/'referee';ref.mkdir();dest=OUT/'supplied_referee';dest.mkdir(exist_ok=True)
    for name in ['check_qubit_comparison.py','independent_checks.py']:
        script=ref/name;shutil.copy2(ROOT/'review/supplied_referee_checks'/name,script);run(script,dest)
    for f in ref.glob('*.json'):shutil.copy2(f,dest/f.name)
(OUT/'rerun_summary.json').write_text(json.dumps({'status':'PASS','programmes':records},indent=2)+'\n')
