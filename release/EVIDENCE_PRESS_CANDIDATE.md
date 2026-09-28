---
title: "A complete gap classification for flat Schmidt-rank-two quantum chains"
subtitle: "Evidence Press candidate release"
date: "28 September 2026 · Version 1.0"
---

**Research status:** AI-assisted manuscript candidate for independent verification. The new classification has not been peer reviewed. This release does not claim an official REF rating or established historical priority.

## The result

A revised Evidence Press candidate gives a necessary-and-sufficient spectral-gap classification for a whole class of quantum chains: every nearest-neighbour rank-one projector interaction whose forbidden two-site state has exactly two equal nonzero Schmidt probabilities. The theorem applies in any finite local dimension. Its substantive new case concerns two distinct Schmidt-support planes whose union spans three dimensions.

A spectral gap separates zero-energy ground states from the lowest positive excitation. Here, “gapped” means that this separation has a positive lower bound independent of the chain's length. The model has open ends, no extra boundary terms and a normalised projector on every bond:

$$
H_N=\sum_{i=1}^{N-1}|\psi\rangle\langle\psi|_{i,i+1}.
$$

The theorem identifies every gapless interaction in the specified Schmidt class. It is gapless exactly when its forbidden vector can be written

$$
\psi=\frac{|u,w\rangle-|w,v\rangle}{\sqrt2},
\qquad w\perp u,v,
$$

where the three vectors are unit vectors. The paper calls this a *balanced marker*: the state $w$ can move between a background of $u$ states on its left and $v$ states on its right. Every such chain has the exact finite-length gap

$$
\gamma_N=1-\cos(\pi/N).
$$

Every other interaction in the class is uniformly gapped. The paper proves explicit positive bounds, rather than inferring them by extrapolating small-chain calculations. The classification concerns the Schmidt rank of the forbidden vector, which is two; the local projector itself has rank one.

## A family whose local spectra never change

The revision completely resolves the family left open in the earlier manuscript:

$$
\psi_\theta=
\frac{\cos\theta\,|00\rangle+\sin\theta\,|01\rangle-|12\rangle}{\sqrt2},
\qquad 0\le\theta\le\pi/2.
$$

For every parameter, the Schmidt probabilities are $(1/2,1/2,0)$. The complete two-site and three-site spectra are also unchanged. Nevertheless,

$$
\theta<\pi/2\quad\Longrightarrow\quad
\gamma_N\ge\frac{\cos^2\theta}{6}>0,
$$

whereas the endpoint has the exact gap $1-\cos(\pi/N)$, which tends to zero.

This is more than a classification of one chosen path. The paper proves that **every** flat-Schmidt qutrit interaction with this specified three-site spectrum has this normal form after applying the same unitary change of basis at every site. It therefore classifies the entire corresponding set of interactions up to that equivalence.

Even the ground-space dimension agrees throughout the family at every length: it is $F_{2N+2}$, where $F_k$ is the Fibonacci sequence. The gap change cannot be detected from the specified short spectra, Schmidt probabilities or finite-length ground-state multiplicity. No equality of the complete spectra at lengths four and above is claimed.

## What the proof adds

For the intersecting-support cases, the ordinary three-site overlap bound reaches its threshold. The new proof examines the vectors that saturate adjacent-pair inequalities. Each pair can separately attain the extremal overlap. On four sites, those extremal vectors need not be compatible with one another and the disjoint-bond constraint.

When the left and right Schmidt supports meet in a line spanned by a unit vector $w$, the decisive invariant is

$$
\tau=2|\langle w,w|\psi\rangle|^2.
$$

For distinct supports, $\tau=0$ identifies the marker case. If $\tau>0$, the incompatibility gives a quantitative positive four-site inequality. A proved open-boundary window sum turns it into a uniform all-length gap. A three-dimensional matrix inside the four-site range gives the sharper bound along the locally isospectral family.

## The earlier literature and the revision

Bravyi and Gosset classified frustration-free qubit chains in 2015 and proposed qutrit rank-one and rank-two chains as a next case [1]. The new theorem settles a specified Schmidt class within that direction, not all qutrit interactions.

The supplied review showed that a weaker locally-isospectral obstruction already follows from the qubit classification. The revised manuscript includes that comparison and does not present it as an independent novelty. It also establishes that local dimension three is minimal for a gapped/gapless separation with **flat** rank-two Schmidt data.

The paper now identifies its dimer and hopping interactions as components of the Motzkin Hamiltonian [2], reconciles the free-Motzkin convention's factor of two [3], and distinguishes the hopping component from the full area-weighted Motzkin model [4]. Deterministic finite-size certification itself is established methodology [5]. The candidate contribution is the classification and its proof, not the invention of these components or methods.

## Evidence and limits

The bundle contains the full manuscript and editable source, an exact-input classifier, 43 exact check groups, seven exact four-site positivity certificates, 146 full-Hamiltonian numerical tests and 24 complex four-site relative-form tests. It also preserves the earlier manuscript and supplied review, reruns their checking programmes, and records a point-by-point response and a source audit. The analytic arguments prove the all-length statements; the computations corroborate finite identities and test implementations.

Complementary results retain a certified neighbourhood in the full complex rank-one projector space, including a full-Schmidt-rank example, and an exponential **upper bound** for an opposing-bias rank-two hopping family. The latter is not a matching asymptotic law. Arbitrary unequal Schmidt data, arbitrary rank-two projectors, periodic gaps and infinite-volume representation-dependent gaps remain outside the classification.

The substantive advance is from examples to a complete class-level decision theorem. The new proofs and the originality claim still require independent specialist assessment.

## Sources

[1] Bravyi, S., & Gosset, D. (2015). Gapped and gapless phases of frustration-free spin-1/2 chains. *Journal of Mathematical Physics, 56*, 061902. <https://arxiv.org/abs/1503.04035>

[2] Bravyi, S., Caha, L., Movassagh, R., Nagaj, D., & Shor, P. W. (2012). Criticality without frustration for quantum spin-1 chains. *Physical Review Letters, 109*, 207202. <https://doi.org/10.1103/PhysRevLett.109.207202>

[3] Salberger, O., Padmanabhan, P., & Korepin, V. (2018). *Non-interacting Motzkin chain—Periodic boundary conditions* [Preprint]. arXiv. <https://arxiv.org/abs/1809.00709>

[4] Andrei, R., Lemm, M., & Movassagh, R. (2026). *The spin-one Motzkin chain is gapped for any area weight t < 1* (Version 2) [Preprint]. arXiv. <https://arxiv.org/abs/2204.04517v2> (Originally submitted 2022.)

[5] Lemm, M. (2019). Gaplessness is not generic for translation-invariant spin chains. *Physical Review B, 100*, 035113. <https://doi.org/10.1103/PhysRevB.100.035113>
