# Flat Schmidt-rank-two chains — Evidence Press candidate v1.0.1

**28 September 2026.** Main manuscript: *A spectral-gap classification for flat Schmidt-rank-two chains: Qutrit saturation geometry, a complete isospectral fibre, and certified extensions*.

## Start here

- `paper/flat_schmidt_chains.pdf`: current manuscript, with editable `.tex` source.
- `release/EVIDENCE_PRESS_CANDIDATE.pdf` and `.md`: preserved v1.0 handoff copy, not the current publication page.
- `AI_INDEX.md`, `ASSURANCE.md`, `REPLAY_RECEIPT.md` and `REVISION_RESPONSE_V101.md`: current v1.0.1 entry points and review dispositions.
- `review/RESPONSE_TO_REVIEW.md`: every requested correction and the new research extensions.
- `review/PROOF_AUDIT_V1.md`: claim dependencies, vulnerable proof steps and uncertainty boundary.
- `sources/SOURCE_AUDIT.md`: primary-source comparisons, versions, search boundary and references.
- `release/REF_DEVELOPMENT_NOTE.md`: substantive development against the supplied review, without assigning a new star rating.

The new theorem classifies exactly the rank-one projector interactions with two equal nonzero Schmidt probabilities. It is not a classification of arbitrary rank-one qutrit states or rank-two projectors. All chains are open, unpinned and projector-normalised. The new proofs are unrefereed and not proof-assistant formalised.

## Evidence map

`evidence/classification_exact.json` records 43 exact groups. `classification_certificates.json` records the seven full-four-site range certificates and positive exact pivots. `classification_numerics.json` records 146 full-Hamiltonian cases and 24 complex relative-form checks. `classifier_tests.json` records 11 exact classifier cases, three rejected out-of-scope inputs and the independent normal-word enumeration.

`evidence/baseline_v0_1/` preserves the previous bundle with its original manifest. `review/supplied_referee_checks/` preserves the supplied referee bundle with its original manifest. Their historical checks concern version 0.1, not the new universal classification. `evidence/reruns/` contains fresh executions of those unchanged programmes, with script hashes and provenance. The independent authorship of the supplied referee code is a property of the supplied material; rerunning it is not a new independent review.

`evidence/RELEASE_CHECKS.json` preserves the supplied v1.0 audit. `REPLAY_RECEIPT.md` records the v1.0.1 publication replay; the separately released JSON receipt additionally binds the final archive, commit and CI. `MANIFEST.sha256` hashes every shipped file in this bundle except itself. Check it before running programmes that overwrite recorded outputs.

## Reproduction

The recorded environment was Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0. These are pinned in `requirements-recorded.txt`; no commercial solver is required. No internet access is used by the check programmes.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-recorded.txt
python code/verify_manifest.py
sh reproduce.sh
```

The reproduction script fixes `PYTHONHASHSEED=0` and single-threaded BLAS for repeatable algebraic ordering and resource use. It runs the new exact checks, classifier tests, new numerical tests and all five legacy/referee programmes. It uses temporary directories for legacy runs and leaves both historical archives unchanged. A fresh run updates output files and timings, so it need not reproduce their hashes byte for byte. The mathematical certificates, programme hashes and pass conditions are the reproducible content; the frozen release manifest applies to the distributed snapshot.

Build the manuscript separately with:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error flat_schmidt_chains.tex
pdflatex -interaction=nonstopmode -halt-on-error flat_schmidt_chains.tex
```

The release PDF can be rebuilt with Pandoc and a LaTeX installation:

```sh
pandoc release/EVIDENCE_PRESS_CANDIDATE.md -s --pdf-engine=pdflatex \
  -V papersize:a4 -V geometry:margin=25mm -V fontsize:11pt \
  -H release/pdf_header.tex -o release/EVIDENCE_PRESS_CANDIDATE.pdf
```

## Exact-input decision utility

`code/classify_flat.py` accepts a **normalised, parameter-free exact SymPy coefficient matrix**. It rejects floats, free symbols and matrices outside the stated Schmidt class. Specialise every parameter to an exact constant first; generic symbolic ranks are not certificates valid at exceptional parameter values. From Python:

```python
import sys
import sympy as s
sys.path.insert(0, 'code')
from classify_flat import classify_flat
M = s.Matrix([[s.Rational(3,5), s.Rational(4,5), 0],
              [0, 0, -1], [0, 0, 0]]) / s.sqrt(2)
print(classify_flat(M))
```

The utility returns a conservative general lower bound, not necessarily the stronger fibre bound proved in the paper. Unresolved symbolic positivity raises an error rather than a guessed phase decision. For disjoint supports the output gives the positive operator-norm bound symbolically.

## Assessment and provenance

The historical development notes concern earlier drafts. The supplied v1.0 review recommended minor revisions, including a concrete classifier repair; `REVISION_RESPONSE_V101.md` records the response. Neither that review nor publication establishes authenticated external peer review or an official REF rating. The source audit does not establish historical priority. See `LICENSES.md` for original-content licences and preserved third-party exceptions.
