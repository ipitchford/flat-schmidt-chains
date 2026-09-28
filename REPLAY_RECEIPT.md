# Publication replay — v1.0.1

Date: 28 September 2026. Kind: producer-side replay; not external peer review.

Environment: Python 3.13.5, SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0. Pinned dependencies in `requirements-recorded.txt`. `reproduce.sh` fixes hash seed and numerical-library thread counts. PDF generation uses pdfLaTeX; it is not a hermetic reproducible build.

Commands and outcomes:

- `sh reproduce.sh`: PASS, 43 exact groups, seven full-four-site certificates, 146 full-Hamiltonian cases, 24 complex checks; classifier cases and all five historical programs.
- `python code/publication_controls.py`: PASS, free-symbol refusal, both reviewer-family specializations, four malformed inputs and deliberate guard-removal mutant rejection.
- `python -OO code/publication_controls.py`: PASS, same explicit controls with Python assertions disabled.
- Supplied v1.0 referee checks, without their historical classifier-bug probe: PASS, four exact full-Gram characteristic polynomials; 50 complex, 16 disjoint-support, 60 weighted-marker and 15 fibre cases. This separate supplied program is not redistributed in this version because no new third-party redistribution permission is inferred.
- Final manuscript: 19 pages; native compiler success, raw-TeX preflight zero findings; every page visually inspected. Layout QA is not proof verification.

`evidence/` contains current exact/numerical reports, preserved older archives and historical audit records. Reproduction overwrites timing-bearing reports; run in a fresh disposable extraction. Frozen-manifest equality is required before replay, not after regenerating timestamps.

The separately released `REPLAY_RECEIPT.json` binds the immutable archive, Git commit, exact-commit Linux CI and final clean-extraction normal/optimized controls. It is outside the archive to avoid circular hashes. Read `ASSURANCE.md` before reuse.
