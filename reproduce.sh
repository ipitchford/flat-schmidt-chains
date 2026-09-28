#!/bin/sh
set -eu
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
python3 code/verify_classification.py > evidence/classification_exact_run.txt 2>&1
cat evidence/classification_exact_run.txt
python3 code/test_classifier.py > evidence/classifier_test_run.txt 2>&1
cat evidence/classifier_test_run.txt
python3 code/check_classification_numerics.py > evidence/classification_numerics_run.txt 2>&1
cat evidence/classification_numerics_run.txt
python3 code/run_legacy_checks.py
