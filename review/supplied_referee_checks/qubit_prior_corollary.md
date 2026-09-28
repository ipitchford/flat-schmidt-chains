# Reviewer-derived qubit comparison

Review date: 28 September 2026.
Source theorem: Bravyi, S., & Gosset, D. (2015). Gapped and gapless phases of frustration-free spin-1/2 chains. Journal of Mathematical Physics, 56, 061902. https://arxiv.org/abs/1503.04035 (Theorem 1).

## Scope of the finding

This is an explicit corollary derived during review, not a claim that the two vectors below were printed in the 2015 paper or previously published elsewhere. It establishes that the unrestricted two-site/three-site/Schmidt-spectrum non-identifiability statement follows readily from the existing qubit classification. It does **not** reproduce the submitted manuscript's flat Schmidt probabilities (1/2,1/2,0), exact three-site spectrum, dimer construction, or genuinely three-dimensional local support.

Let

\[
\chi_c=2^{-1/2}|00\rangle+\tfrac12|01\rangle-\tfrac12|10\rangle,
\]
\[
\chi_g=\tfrac12|00\rangle+\tfrac{1+\sqrt5}{4}|01\rangle
+i\tfrac{\sqrt5-1}{4}|10\rangle.
\]

Both are normalised. The squared Schmidt coefficients are
\((2+\sqrt3)/4,(2-\sqrt3)/4\). Both H2 spectra are \(0^{(3)},1\).
For either vector, the H3 characteristic polynomial is

\[
x^4\left((x-1)^4-\frac38(x-1)^2+\frac1{256}\right).
\]

Equivalently, the four positive eigenvalues are
\(1\pm(\sqrt2+1)/4\) and \(1\pm(\sqrt2-1)/4\), with four zero eigenvalues.
The accompanying exact SymPy verifier checks the polynomial directly on the 8 by 8 Hamiltonian over algebraic number fields; it does not merely assume the singular-value formula.

The Bravyi--Gosset transfer matrix is

\[
T_\chi=\begin{pmatrix}\bar\chi_{01}&\bar\chi_{11}\\-\bar\chi_{00}&-\bar\chi_{10}\end{pmatrix}.
\]

For chi_c both transfer eigenvalues are 1/2. For chi_g their moduli are
\((\sqrt5+1)/4\) and \((\sqrt5-1)/4\). The cited theorem therefore makes the first family gapless and the second uniformly gapped. The gapless assertion here uses the theorem's 1/(N-1) upper bound, not an unproved exact gap formula.

Adding an unused third local level preserves both conclusions: each pattern of spectator sites reduces the Hamiltonian to a sum of open qubit-segment Hamiltonians. The embedded pair has equal H2 and H3 spectra and equal Schmidt spectra with an added zero. This supplies a lower-dimensional antecedent for the broad qutrit obstruction.

## Why the flat-Schmidt condition remains substantive

For a two-qubit forbidden vector with Schmidt probabilities (1/2,1/2), its coefficient matrix is M=U/sqrt(2), with U unitary. Writing J=[[0,1],[-1,0]], the Bravyi--Gosset matrix is J conjugate(M)^T, hence a unitary matrix divided by sqrt(2). Both transfer eigenvalues have modulus 1/sqrt(2), so every such qubit chain is gapless.

Consequently, a gapped/gapless separation under *flat rank-two Schmidt data* cannot occur at local dimension two. The submitted qutrit theorem gives it at dimension three. This dimension-minimal formulation sharpens the contribution without claiming a general classification.

## Suggested manuscript action

Add the qubit comparison (or an equivalent example), explicitly distinguish the restricted flat-Schmidt result from the unrestricted no-go, and consider adding the dimension-minimality corollary. The finding concerns positioning and originality; it does not invalidate Theorem 2.1.
