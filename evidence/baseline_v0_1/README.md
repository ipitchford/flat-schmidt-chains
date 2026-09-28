# Locally isospectral qutrit chains with different spectral-gap phases

**Evidence Press research manuscript candidate — version 0.1 — 28 September 2026**

Start with `paper/qutrit_gaps.pdf` (11 pages). The editable mathematical source is
`paper/qutrit_gaps.tex`. All claims concern open chains with no added boundary
terms and with each local interaction normalized to be an orthogonal projector.

## Results

The balanced rank-one forbidden vectors `(00 - 12)/sqrt(2)` and
`(01 - 12)/sqrt(2)` have identical two-site and three-site spectra and identical
Schmidt probabilities. Their open-chain gap behavior nevertheless differs:
the first has gap at least 1/4 at every length; the second has exact gap
`1 - cos(pi/N)`. A continuous interpolation keeps all these local spectral
data fixed. This is an obstruction to classification using only these data,
not an obstruction to longer finite-size criteria or to using eigenvectors.

The manuscript also proves an exact marker-family formula, a uniformly gapped
positive-weight dimer family, a rank-one projector ball of radius 1/90 with
uniform gap at least 1/20, an explicit full-Schmidt-rank example outside the
three-site test, and exponentially closing gaps for rank-two opposing-bias
chains even though each rank-one constituent is gapped.

**This is a partial solution of the Bravyi–Gosset qutrit problem, not the full
classification of arbitrary rank-one or rank-two interactions.** It follows
the partial-map target in the supplied Problem 5 brief. Deterministic gap
criteria are established prior work, particularly Lemm (2019), and are not
claimed as new here. The paper is AI-assisted and unrefereed. Historical
priority is unconfirmed. No outside referee or formal proof assistant has
verified the work.

## Reproduction

Python 3.10 or later is recommended. The exact verifier needs only SymPy:

```sh
python -m pip install sympy==1.14.0
python code/verify_exact.py
python code/check_sector_structure.py
```

The recorded run passed **27 exact check groups**, including 50 exact
one-vacancy trial-state certificates at chain lengths 3, 5, ..., 101.
The standard-library sector diagnostic checked all **9,840** words at lengths
1 through 8. The proofs for arbitrary chain length are in the manuscript;
finite tests are not treated as proof of an asymptotic claim.

For optional floating-point diagnostics:

```sh
python -m pip install numpy==2.3.5 scipy==1.17.0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/check_numerics.py --max-n 6
```

The recorded numerical run passed 35 cases (seven models, lengths 2–6).
`requirements-recorded.txt` records the tested package versions; the full
recorded environment was Python 3.13.5. Numerical diagonalization uses a
1e-9 zero threshold and a 1e-8 comparison tolerance. Those tolerances play
no role in the exact certificates or analytic proofs.

Build the paper with an ordinary LaTeX installation:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error qutrit_gaps.tex
pdflatex -interaction=nonstopmode -halt-on-error qutrit_gaps.tex
```

## Contents and evidence boundary

- `paper/`: PDF and LaTeX source, with all proofs and five primary references.
- `code/verify_exact.py`: exact projectors, characteristic polynomials,
  four-site decomposition, rational LDL factorization, stability arithmetic,
  heat-bath identities, trial vectors, and symbolic rank-two overlaps.
- `code/check_sector_structure.py`: independent exhaustive check of the
  frozen-symbol/monomer–dimer decomposition through eight sites.
- `code/check_numerics.py`: separately implemented full-matrix diagnostics.
- `evidence/`: machine-readable certificates, check reports, CSV values,
  and recorded console outputs.
- `PROOF_AUDIT.md`: internal audit of the load-bearing arguments and limitations.
- `SOURCE_SCOPE.md`: verified primary-source scope and the correction to the brief.
- `MANIFEST.sha256`: file-integrity hashes, excluding the manifest itself.

The exact verifier regenerates its JSON reports. The numerical and sector
scripts regenerate their respective diagnostics. Regenerated reports may
record different environment versions; the manuscript does not depend on
a particular floating-point eigensolver.

No third-party paper PDFs, font files, private user profile information, or
unrelated source-brief material are included. Nothing has been published or
uploaded to evidencepress.org by this workflow.
