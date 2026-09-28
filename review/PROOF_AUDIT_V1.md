# Proof and uncertainty audit — version 1.0

**Date:** 28 September 2026. **Nature:** internal mathematical audit, not independent peer review or proof-assistant verification.

## Claim dependencies

| Claim | Load-bearing argument | Computational corroboration | Boundary |
|---|---|---|---|
| Complete flat-Schmidt-rank-two classification, Theorem 2.1 | Support geometry; unique extremal adjacent-pair mode; Lemmas 4.1–4.2; exact marker sector | Exact contractions, genuinely complex cases, full-range four-site certificates; seeded complex tests | Exactly two equal nonzero Schmidt probabilities; open chains |
| Quantitative bound $3\tau(2-t)(1-t)/1024$ | Pair-kernel approximation errors; double-projection obstruction; clipped-window summation | Four exact general examples and 24 complex relative-form tests | Conservative lower bound, not an optimal gap or exponent |
| Entire fibre normal form and gap, Theorem 5.1 | Principal angles; phase reduction of a $2\times2$ unitary; three-dimensional Gram core | Exact reducing core, characteristic polynomial, principal minors; three full-range exact certificates | The specified two-/three-site spectra and flat Schmidt data |
| Constant ground-space dimension, Proposition 5.2 | Terminating non-overlapping rewrite $12\mapsto c00+s01$ | Independent normal-word enumeration through length eight | Dimension, not equality of ground spaces or longer spectra |
| Dimer gap | Complete component decomposition; reversible hard-core heat-bath comparison | Original exact checks and independent supplied finite heat-bath checks rerun | Positive dimer weights; bound not sharp |
| Complex rank-one neighbourhood | Rank-maximality lemma; exact five-state positivity; Weyl inequality; finite-size bound | Original exact certificates rerun | Fixed local rank one; no arbitrary rank changes |
| Opposing-bias exponential upper bound | Reducing one-vacancy sector; exact orthogonality; bottleneck trial state | 50 original exact sizes, plus 24 supplied additional trials rerun | Upper bound only; a specified two-parameter family |

## High-risk steps inspected

**Complex conjugation.** The right reduced density matrix is $M^T\overline M$, not $M^*M$ in the physical on-site basis. The overlap is $(\overline M M)^T$. The exact input utility uses these conventions. The proof retains arbitrary complex coefficients in the unitary Schmidt frame. Both $\langle\psi|\ell\ell\rangle$ and $\langle\psi|rr\rangle$ equal $c/\sqrt2$ in that frame. Complex on-site rotations are included in the numerical tests and exact classifier regression.

**Uniqueness of the saturated local mode.** For distinct intersecting supports, the nonzero overlap singular values are $1/2,t/2$ with $t<1$. The eigenvalue $1/2$ of the two-projector sum is therefore simple. Its eigenvector, rather than a guessed ground state, controls both overlapping pair kernels. The proof treats coincident supports separately; it does not divide by $1-t$ there.

**The four-site identity.** With $h=p_1+p_2+p_3$, the positive operator is

$$
\mathcal G=\mathcal A(p_1,p_2)+\mathcal A(p_2,p_3)+2p_1p_3
=h^2-\tfrac12(p_1+p_3).
$$

There is no subtraction of $p_2$. The exact verifier checks this identity. Omitting the positive disjoint product would invalidate the obstruction argument.

**Boundary accounting.** The window sum uses zero-extended bond projectors. A clipped two-bond window has least comparison coefficient $(3-\sqrt5)/4$, rather than the full-window coefficient by fiat. Every bond occurs three times on the comparison side. The difference between twice $H_N^2$ and the summed window operators contains only positive products of disjoint commuting projectors. The coefficient identity is checked at lengths 2–30; the analytic count proves it for all lengths.

**The negative Gram direction.** The fibre certificate has one negative direction in the redundant 27-column range representation. It is explicitly $(\psi,0,-\psi)$, lies in $\ker C$, and is orthogonal to $\operatorname{ran}C^*$. It is not discarded from a physical Hilbert space by assumption. After its removal, all blocks have the stated lower bounds. The full physical four-site form is checked by exact positive pivots on a 26-dimensional range basis.

**Kernel stability.** A norm-continuity estimate alone does not prove persistence of a gap above a degenerate zero space. The retained neighbourhood proof uses universal local rank maxima attained at the dimer point. Only after this step does it apply Weyl's inequality to the smallest positive eigenvalues.

**Global variational orthogonality.** The rank-two trial state is orthogonal to the unique zero mode inside a reducing sector. This implies orthogonality to the full global ground space. Orthogonality merely to one product ground state would be insufficient.

## Sanity checks

The three-site multiplicities satisfy $21+1+4+1=27$ and the trace is $1/2+4+3/2=6$. The fibre Gram blocks have dimensions $5+4(2)+10+4=27$; the killed negative direction leaves the expected 26-dimensional four-site range. The core has determinant $c^2/4$ and sum of pairwise eigenvalue products $9/4$, giving its lower bound $c^2/9$. Multiplication by the window factor $3/2$ gives $c^2/6$.

At two sites every normalised rank-one projector has gap one. At the marker endpoint the formula gives $1-\cos(\pi/2)=1$. At $N=6$ it gives approximately $0.1339745962$, reproduced by full diagonalisation. The normal-word recurrence gives dimensions $3,8,21,55,144,377$ at lengths one through six, including both endpoints and all intermediate parameters.

## What the tests do not establish

Seven exact example certificates are not a universal quantified proof. The 146 full-Hamiltonian tests and 24 relative-form tests use floating-point arithmetic and cannot decide a limiting gap. The all-parameter and all-length statements rely on the analytic manuscript. The supplied referee checked the previous manuscript, not the new classification. Fresh reruns of that referee's code do not create a fresh independent review.

## Remaining research boundaries

The principal theorem does not classify unequal Schmidt probabilities, arbitrary full-Schmidt-rank qutrit interactions, or arbitrary rank-two local projectors. The retained full-complex neighbourhood is a sufficient certificate only. The matching full-chain lower bound in the opposing-bias family was not obtained. Periodic and infinite-volume representation-dependent gaps were not analysed. The fibre bound proves positivity and its explicit lower scale; it does not identify an exact thermodynamic gap or critical exponent.

Historical priority is not settled by a search that fails to find an equivalent theorem. A specialist comparison and an independent adversarial reading of the saturation proof are the most consequential external checks. No REF star rating follows from this audit.
