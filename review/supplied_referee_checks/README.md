# Qutrit-gap manuscript: reviewer verification record

Date: 28 September 2026.
Target: `evidence_press_qutrit_gaps_v0_1(1).zip`, manuscript version 0.1.

## Scope

The manuscript and analytic proofs were reviewed, the submitted scripts were inspected and rerun in a separate copy, and the independent checks here were written without importing the submitted implementation. No source manuscript was modified, and nothing was published or uploaded to Evidence Press.

These files accompany an academic review. They are not a formal proof-assistant verification, a second human referee report, an exhaustive literature search, or an official REF assessment. Finite checks do not prove all-length assertions.

## Results

- All 19 original manifest entries matched.
- All 27 submitted exact check groups passed.
- Submitted sector enumeration passed on all 9,840 words of lengths 1 through 8.
- All 35 submitted numerical cases passed.
- Independent direct word-basis construction passed on 20 full Hamiltonians.
- Independent complex perturbation tests passed on 18 short chains (six perturbations, lengths 2, 3, 4), preserving the relevant maximal ranks.
- Independent hard-core heat-bath tests passed on 50 finite systems: path lengths 1 through 10 and activities 0.01, 0.1, 1, 10, 100.
- All 24 additional opposing-bias Rayleigh trials passed exact rational orthogonality and energy-identity checks. Evaluations of the exponential upper bound used floating-point logarithms and are labelled diagnostics.
- The reviewer-derived qubit comparison passed exact normalisation, reduced-density determinant, overlap invariant, full H3 characteristic polynomial, and transfer-eigenvalue checks.

The qubit comparison is the principal substantive finding. It shows that the *unrestricted* local-spectral non-identifiability result is already a short corollary of Bravyi--Gosset (2015). It does not duplicate the submitted flat-Schmidt, genuinely qutrit construction. See `qubit_prior_corollary.md` for the mathematical argument and the precise attribution boundary.

## Reproduction

The recorded environment was Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0.

```
python check_qubit_comparison.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python independent_checks.py
```

For the submitted-script reruns, use the unchanged scripts in the original uploaded bundle:

```
python code/verify_exact.py
python code/check_sector_structure.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_numerics.py --max-n 6
```

The original submitted scripts are not reproduced here. Their new console logs and regenerated JSON/CSV outputs are included, under `submitted_rerun_outputs/` where applicable. No third-party papers or fonts are included.

## Inspection and literature limits

The 11-page manuscript, its LaTeX source, all three verification scripts, the source-scope note, internal audit, and supplied evidence were inspected. Primary literature was checked with live web and Exa searches, focusing on exact local terms, boundary conditions, rank, and normalisation. Relevant theorem/definition sections were inspected rather than purporting to re-referee every external paper. The browser's PDF screenshot requests failed for the Motzkin and PVBS comparison papers; their accessible parsed full texts supplied the definition-level comparisons. The main manuscript's local PDF render was inspected successfully.

No fatal mathematical defect was found. The editorial recommendation is major revisions, principally for substantive contribution positioning and missing direct Motzkin/free-Motzkin comparisons. Indicative overall REF quality: 3*, with material 2*/3* uncertainty tied to originality and significance. This is not a claim of an official assessment or assured journal acceptance.
