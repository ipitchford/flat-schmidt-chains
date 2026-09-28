# Internal proof audit

This is a development audit, not an independent external referee report.
All universal statements require checking the analytic proofs in the paper;
the finite verifier is not a proof assistant.

## Load-bearing checks

**Ground-space degeneracy in upper bounds.** The marker spectrum is obtained
on an explicitly reducing subspace. For rank two, the one-vacancy sector is
reducing and its kernel is exactly the line spanned by the positive vector g.
The trial vector is orthogonal to that line, hence to the entire global kernel.
No Rayleigh quotient is taken against only a selected product ground state.

**Ground-space degeneracy under perturbation.** Weyl's inequality alone would
not exclude tiny positive eigenvalues lifted from a degenerate kernel. The
four-site argument additionally uses universal rank maxima 1, 6, and 26,
attained at the center. These prevent extra positive eigenvalues for the
short chains once the original positive eigenvalues remain positive.
No assertion of all-length kernel stability is needed.

**Open rather than periodic boundaries.** The finite-size proof includes
clipped windows at both ends; every bond occurs exactly m-1 times. The gap
input is the minimum over all open subchains of lengths 2 through m. This
avoids importing a periodic-only threshold or omitting an edge gap.

**Dimer sectors.** Frozen 1/2 symbols cannot be changed by 00 ↔ 12. The
remaining intervals have monomer–dimer tilings. The corresponding diagonal
ground-state transform has insertion rate a^2 and deletion rate b^2, not
the reverse. Each two-site heat-bath block has nonzero gap at least b^2.
The pair-block coupling contracts at rate at least 2b^2; comparison then
gives b^4. A separate four-site rational proof establishes the flagship
balanced dimer's gappedness even without the sharper heat-bath estimate.

**Short-chain isospectrality.** The rank-one contraction has singular values
1/2, 0, 0 throughout the interpolation. The full three-site spectrum,
including the 21-dimensional kernel, is stated. Equality is not claimed
for four-site spectra or for eigenvectors. Neither equality of Schmidt
spectra alone nor equality of two- and three-site energy spectra identifies
the thermodynamic gap phase.

**Rank-two overlap multiplicities.** The symbolic check verifies the complete
six-value singular spectrum: the two same-species squared singular values
each occur twice, and the two cross-species values each occur once. This
supports the norm formula; omitted zero modes or mistaken multiplicities
are not used in the paper.

**Translation invariance.** Opposing biases are encoded by a fixed ordered
particle sector of one spatially homogeneous local Hamiltonian. There is
no spatially varying interaction hidden in the construction. The effective
birth–death problem in that sector is inhomogeneous.

**Comparison with PVBS.** The rank-two model has no same-species penalty and
no unlike-species interchange. Statements proved for full PVBS models
cannot be transferred by dropping their additional positive terms, because
that changes the ground space.

## Limits that remain

The full arbitrary-projector classification is not established. Neither the
complete isospectral interpolation nor all same-direction two-species biases
are classified. No assertion is made about periodic chains, bulk GNS gaps,
stability to unconstrained nonprojector perturbations, or a general criterion
based only on Schmidt data. The exact factorization is a finite arithmetic
certificate, not a formal verification of the analytic heat-bath theorem.

Historical priority, novelty relative to all rewriting/clock/Markov-chain
literature, and journal/REF significance require subject-specialist review.
The search correction in SOURCE_SCOPE.md is substantive: deterministic
qutrit gap regions were available before this work.
