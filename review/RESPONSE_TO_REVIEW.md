# Response to the supplied review

**Manuscript:** *A spectral-gap classification for flat Schmidt-rank-two chains*. Version 1.0, 28 September 2026.  
**Review being addressed:** *Locally isospectral qutrit chains with different spectral-gap phases*, version 0.1, supplied 28 September 2026.

The revision implements both major comments and all three minor comments. It also proves a complete classification of the flat-Schmidt-rank-two class and resolves the interpolation proposed for further research. The supplied review and its checks are preserved, not retrospectively represented as assessments of these new proofs.

## Major comment 4.1: the qubit precedent and the actual originality claim

**Actioned.** Section 5.3 includes both explicit qubit vectors, their Schmidt probabilities, their common three-site characteristic polynomial and the distinct transfer-matrix moduli. It credits the explicit comparison to the supplied review, and attributes the underlying classification to Bravyi–Gosset. It does not claim that the vectors were printed in the 2015 paper. The referee's exact verifier has been rerun successfully.

The abstract, introduction and release no longer present the unrestricted local-spectral obstruction as an independent novelty. The principal candidate contribution is Theorem 2.1: a necessary-and-sufficient gap classification of **every** rank-one interaction whose forbidden vector has exactly two equal nonzero Schmidt probabilities, in any finite local dimension. The new case is the three-dimensional span of distinct, intersecting Schmidt supports. All gapless members have an exact finite-chain gap. Gapped members have explicit positive lower bounds.

Corollary 2.2 states the requested minimal-dimension result. In dimension two the Schmidt supports coincide, and every flat rank-two forbidden vector is a balanced marker after an on-site basis choice. The chain is gapless. The qutrit dimer and marker then establish that dimension three is minimal for the flat-Schmidt locally-isospectral separation.

## Major comment 4.2: Motzkin and free-Motzkin antecedents

**Actioned at the level of the local operators.** Section 8.5 writes the forbidden vectors and compares ranks, energy units, boundary conditions and kernels.

The original Motzkin bulk projector is exactly the sum of the balanced dimer term and the unbiased rank-two hopping projector in our normalisation. Its pinning terms are stated. Moreover, inspection of the 2012 proof shows that the hopping reduction to the ferromagnetic chain and the formula $1-\cos(\pi/N)$ were already used there. The revision acknowledges that earlier result, not merely the 2018 antecedent.

The Salberger–Padmanabhan–Korepin free-Motzkin paper uses periodic boundaries. Its displayed local difference-vector outer products equal twice our normalised projectors; the relation $e_j^2=2e_j$ confirms the factor. We do not transfer a periodic gap assertion to open chains or compare unconverted energies.

For area weight $s$, the full deformed Motzkin bulk interaction is

$$
P(s,s^{-1})+\frac{|12-s00\rangle\langle12-s00|}{1+s^2}.
$$

The Andrei–Lemm–Movassagh gap theorem for $0<s<1$ concerns the full model, not its hopping component alone. The version inspected is arXiv:2204.04517v2, revised 23 May 2026. The present exponential upper bound applies to the first summand without pinning. The manuscript now explains the enlarged conserved-word kernel after deleting pair creation. The distinction from the full two-species PVBS model is retained.

The comparison does not establish historical priority of the new classification or the quantitative opposing-bias theorem. It identifies exactly what is and is not supplied by these antecedents.

## Minor comments and presentation changes

| Comment | Implemented change |
|---|---|
| 7.1: exponential upper bound versus asymptotic law | Theorem 8.1 and the release explicitly say **exponential gap upper bound**. No matching lower bound, optimal exponent or asymptotic identification of the full-chain gap is claimed. |
| 7.2: two meanings of an open region | Theorem 7.1 concerns the full complex rank-one projector space. Section 8.4 explicitly confines the opposing-bias open region to its two-parameter family and disclaims arbitrary rank-two perturbation stability. |
| 7.3: explicit size threshold | Theorem 8.1 uses $N\ge2+\lceil B/A\rceil$, where $A=-\log a$ and $B=\log b$. This ensures the cut lies strictly inside the one-vacancy word. |
| 7.3: meaning of local isospectrality and phase | Section 1 fixes open-chain gaps and no boundary terms. Theorem 5.1 specifies the complete two- and three-site spectra; no equality of longer spectra is asserted. |
| Revision plan: rank maximality | Lemma 7.3 isolates the short-chain rank maxima and their attainment, before the Weyl argument. This prevents new positive eigenvalues emerging from the kernel. |

## Research extensions completed

**Theorem 2.1: a complete classification, not only further examples.** If the physical Schmidt supports intersect in the line spanned by a unit vector $w$, define $\tau=2|\langle w,w|\psi\rangle|^2$. The gapless set is exactly $\tau=0$. A quantitative obstruction to simultaneously saturating two adjacent-pair inequalities proves a uniform gap when $\tau>0$. The disjoint-support case is covered by the standard overlap criterion; coincident supports reduce to the marker family. Lemmas 4.1 and 4.2 contain the new all-length argument.

**Theorem 5.1: the entire short-spectrum fibre.** All flat-Schmidt qutrit interactions with the specified three-site spectrum have, up to a common on-site unitary, the unique normal form

$$
\psi_\theta=(\cos\theta\,00+\sin\theta\,01-12)/\sqrt2,
\quad0\le\theta\le\pi/2.
$$

Every $\theta<\pi/2$ is uniformly gapped, with lower bound $\cos^2\theta/6$. The endpoint has exact gap $1-\cos(\pi/N)$. The three-dimensional certificate embedded in the four-site range proves the improved bound analytically for the whole parameter interval.

**Proposition 5.2: fixed degeneracy at every length.** The ground-space dimension on this fibre is $F_{2N+2}$, independently of $\theta$. Thus the endpoint change is not explained by a jump in finite-length ground-state degeneracy.

## Evidence and assessment boundary

The new exact checks, numerical diagnostics, old programme reruns and supplied-referee programme reruns all pass. The archive distinguishes their provenance. The new classifier is for exact inputs and rejects floating-point data; the numerical zero threshold is not a phase decision rule.

The referee's suggested matching lower bound for the opposing-bias full-chain gap was not established. The broader arbitrary-rank-one and arbitrary-rank-two qutrit problems are not solved here. The classification above is the substantive advance submitted for renewed assessment. No revised REF rating or external endorsement is attributed to the supplied referee.
