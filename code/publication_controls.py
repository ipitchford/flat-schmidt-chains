"""Explicit semantic regression and mutation controls, also active under -OO."""
from pathlib import Path
import json, shutil, subprocess, sys, tempfile
import sympy as s
from classify_flat import classify_flat

root=Path(__file__).resolve().parents[1]
def require(value, message):
    if not value: raise RuntimeError(message)
x=s.Symbol('x',real=True)
M=s.Matrix([[(1-x*x)/(1+x*x),0,2*x/(1+x*x)],[0,-1,0],[0,0,0]])/s.sqrt(2)
try: classify_flat(M)
except ValueError as exc: require('Free symbols' in str(exc),'wrong rejection')
else: raise RuntimeError('symbolic family accepted')
require(classify_flat(M.subs(x,0))['classification']=='gapless','endpoint misclassified')
require(classify_flat(M.subs(x,1))['classification']=='uniformly_gapped','interior misclassified')
for bad in [s.zeros(3),2*M.subs(x,0),s.eye(3)/s.sqrt(3),M.subs(x,0).evalf()]:
    try: classify_flat(bad)
    except ValueError: pass
    else: raise RuntimeError('invalid domain accepted')
# Prove the regression suite notices removal of the repaired domain boundary.
with tempfile.TemporaryDirectory(prefix='flat-schmidt-mutation-') as temp:
    dest=Path(temp);(dest/'code').mkdir();(dest/'evidence').mkdir()
    source=(root/'code/classify_flat.py').read_text()
    original="    if M.free_symbols:\n        raise ValueError('Free symbols are not supported; specialise parameters to exact constants before classification.')\n"
    require(original in source,'mutation target missing')
    (dest/'code/classify_flat.py').write_text(source.replace(original,''))
    shutil.copyfile(root/'code/test_classifier.py',dest/'code/test_classifier.py')
    result=subprocess.run([sys.executable,'-OO',str(dest/'code/test_classifier.py')],capture_output=True,text=True,timeout=90)
    require(result.returncode!=0 and 'Unspecialised family accepted' in result.stderr,'mutation escaped regression')
print(json.dumps({'status':'PASS','optimized':not __debug__,'symbolic_boundary':True,'specialisations':2,'invalid_inputs':4,'removed_guard_rejected':True}))
