# Academic review: *Locally isospectral qutrit chains with different spectral-gap phases*

**Manuscript:** Evidence Press, version 0.1, 28 September 2026.
**Recommendation:** **Major revisions**, principally to establish the contribution’s precise relationship to prior work.
**Prospective REF assessment:** **3***, with material uncertainty at the **2*/3*** boundary. The present evidence does not support 4*.

[Download the independent referee checks, exact qubit comparison and execution logs](sandbox:/mnt/data/qutrit_referee_checks_2026-09-28.zip).

## 1. Executive assessment

This manuscript proves several results for open, translation-invariant, frustration-free qutrit chains. Its strongest construction pairs two rank-one interactions with identical two-site spectra, three-site spectra and flat rank-two Schmidt data, while one chain remains uniformly gapped and the other has gap \(1-\cos(\pi/N)\). Supporting results include an exactly solvable marker family, a uniformly gapped dimer family, a rational four-site stability certificate and an opposing-bias rank-two family with exponentially small gap upper bounds.

**I found no fatal mathematical defect.** All supplied verification programmes passed when rerun. Independently written checks also passed. The treatment of ground-space degeneracy in the perturbation argument is particularly important and appears correct.

The principal weakness concerns originality and positioning. During review, I constructed and exactly verified a different locally isospectral gapped/gapless pair using Bravyi–Gosset’s existing qubit classification. Thus the unrestricted local-spectral obstruction is already a short corollary of that classification. This does **not** reproduce the manuscript’s flat Schmidt spectrum or genuinely qutrit construction. ([arXiv][1])

The manuscript also omits directly relevant Motzkin and free-Motzkin comparisons. These omissions require substantive revision, although they do not invalidate the proofs. My assessment is therefore a mathematically credible specialist paper whose strongest new contribution needs sharper isolation before publication.

## 2. Scope and evidence limits

I inspected the **11-page manuscript**, its complete LaTeX source, all three verification programmes, the internal proof audit, source-scope statement, release documentation and supplied evidence. All **19 entries in the original integrity manifest matched**.

The assessment concerns the paper’s stated model:

$$
H_N(P)=\sum_{i=1}^{N-1}P_{i,i+1},
$$

with open boundaries, no additional boundary terms and orthogonal-projector normalisation. Its gap is the smallest strictly positive eigenvalue. The review does not extend these conclusions to periodic chains, infinite-volume representations, arbitrary perturbations of interaction rank or a complete qutrit classification.

I assessed the work as a theoretical mathematical-physics paper suitable for a specialist research journal. No target journal supplied additional criteria. Empirical-design and statistical-inference criteria are inapplicable.

The supplied computations were rerun in a separate copy. I also wrote independent implementations rather than relying exclusively on the authors’ tests. Nevertheless, the all-length conclusions rest on the analytic arguments. Neither the manuscript nor this review constitutes proof-assistant verification. The literature search was targeted, and historical priority remains less secure than the internal mathematical assessment.

## 3. Contribution and positioning

The strongest defensible central statement is:

> **Flat rank-two Schmidt data, together with complete two-site and three-site spectra, do not determine whether a rank-one qutrit chain has a uniform open-chain spectral gap.**

The manuscript establishes this using

$$
\psi_{\mathrm d}=\frac{|00\rangle-|12\rangle}{\sqrt2},
\qquad
\psi_{\mathrm m}=\frac{|01\rangle-|12\rangle}{\sqrt2}.
$$

Theorem 2.1 gives

$$
\gamma_N(P_{\mathrm d})\ge\frac14,
\qquad
\gamma_N(P_{\mathrm m})=1-\cos\frac{\pi}{N}.
$$

The continuous family in §5 strengthens the example: the specified local spectral data remain fixed along the interpolation. The paper appropriately leaves the intermediate gap classification unresolved.

Theorem 2.2 supplies a different kind of result. Its four-site certificate proves a neighbourhood in the **full complex rank-one projector space**, including a full-Schmidt-rank example outside the elementary three-site criterion. The significance lies in the explicit certificate and its carefully controlled perturbation argument. Deterministic neighbourhood certification itself predates this manuscript, as its introduction correctly acknowledges. ([arXiv][2])

Theorem 2.3 provides an explicit mechanism by which two individually gapped hopping constraints jointly admit very low-energy excitations. Its force is quantitative and structural: conserved particle order creates a one-vacancy sector with a bottleneck. It establishes an exponential **upper bound**, not a matching asymptotic formula.

These results form a coherent partial investigation. They do not yet establish a general classification principle for arbitrary qutrit projectors.

## 4. Major comments

### 4.1. Isolate the flat-Schmidt qutrit result from a weaker obstruction already obtainable from the qubit classification

**Issue.** The general assertion that two-site spectra, three-site spectra and Schmidt probabilities fail to determine gap behaviour is not independent of the established qubit classification.

**Manuscript evidence.** The introduction identifies the “locally isospectral separation” as a candidate contribution; Theorem 2.1 concludes that no necessary-and-sufficient classifier using only these data can handle all rank-one qutrit chains. The abstract already reports the flat Schmidt probabilities, but the positioning does not explain why that restriction matters.

**Independent comparison.** Consider the normalised two-qubit states

$$
\chi_{\mathrm c}
=\frac{1}{\sqrt2}|00\rangle
+\frac12|01\rangle-\frac12|10\rangle,
$$

$$
\chi_{\mathrm g}
=\frac12|00\rangle
+\frac{1+\sqrt5}{4}|01\rangle
+i\frac{\sqrt5-1}{4}|10\rangle.
$$

My exact verification establishes that both have Schmidt probabilities

$$
\left(\frac{2+\sqrt3}{4},\frac{2-\sqrt3}{4}\right),
$$

the same two-site spectrum and the same three-site characteristic polynomial:

$$
\det(xI-H_3)
=x^4\left((x-1)^4-\frac38(x-1)^2+\frac1{256}\right).
$$

For the Bravyi–Gosset transfer matrix

$$
T_\chi=
\begin{pmatrix}
\overline{\chi_{01}}&\overline{\chi_{11}}\\
-\overline{\chi_{00}}&-\overline{\chi_{10}}
\end{pmatrix},
$$

the first state has two eigenvalues of modulus \(1/2\). The second has eigenvalue moduli

$$
\frac{\sqrt5+1}{4},
\qquad
\frac{\sqrt5-1}{4}.
$$

Bravyi–Gosset’s Theorem 1 therefore makes the first chain gapless and the second uniformly gapped. ([arXiv][1])

Adding an unused third local level preserves the distinction: spectator sites split the Hamiltonian into open qubit segments. This also yields a qutrit pair with matching short-chain and Schmidt spectra.

**Attribution boundary:** I derived this explicit comparison during the review. I am **not** claiming that these vectors were printed in the 2015 paper or previously published elsewhere. The finding shows that the unrestricted obstruction is a short consequence of existing theory.

**Why it matters.** The manuscript’s distinctive contribution survives, but in a more specific form. Its probabilities are \((1/2,1/2,0)\), and its interactions require three local dimensions. Those features should carry the originality argument.

Indeed, a useful strengthening follows. A two-qubit state with Schmidt probabilities \((1/2,1/2)\) has coefficient matrix \(M=U/\sqrt2\), with \(U\) unitary. Its Bravyi–Gosset transfer matrix is also unitary up to the factor \(1/\sqrt2\), so both eigenvalues have equal nonzero modulus. Every such qubit chain is therefore gapless. Combining this observation with Theorem 2.1 shows that **local dimension three is minimal for a gapped/gapless separation with flat rank-two Schmidt data**.

**Required revision.** Add the qubit comparison, distinguish the restricted result from the unrestricted corollary, and consider stating the dimension-minimality observation explicitly. The exact verification and derivation are included in the referee bundle. No change to the validity of Theorem 2.1 is required.

### 4.2. Compare the actual local projectors with the Motzkin and free-Motzkin literature

**Issue.** The closest omitted literature shares the manuscript’s local terms. This requires a definition-level comparison, rather than a general acknowledgement of rewriting Hamiltonians.

**Manuscript evidence.** Sections 4 and 7 analyse the dimer projector and the two-species hopping projector. The five references contain no Motzkin or free-Motzkin paper.

The original Motzkin construction uses three forbidden vectors proportional to

$$
|00\rangle-|12\rangle,\qquad
|01\rangle-|10\rangle,\qquad
|02\rangle-|20\rangle.
$$

Thus, with matching normalisation and considering the bulk interaction,

$$
P_{\mathrm{Motzkin}}
=P_{\mathrm d}+P(1,1).
$$

The manuscript’s balanced dimer term and unbiased rank-two hopping terms are complementary components of this established model. ([quantum.physics.sk][3])

Salberger, Padmanabhan and Korepin explicitly study the **hopping-only** free-Motzkin model with periodic boundaries. Their local operators have a different overall normalisation, which must be reconciled before comparing gaps. This is a direct antecedent for the unbiased rank-two model, although it does not by itself establish the present opposing-bias open-chain theorem. ([arXiv][4])

There is also a precise deformed comparison. The hopping part of the area-weighted Motzkin interaction is \(P(t,t^{-1})\), up to irrelevant signs of the forbidden vectors. Andrei, Lemm and Movassagh prove a uniform gap for the **full** open-boundary Motzkin interaction when \(0<t<1\). The present rank-two theorem instead makes its hopping-only part gapless in this parameter range. The distinction concerns the omitted pair-creation projector and the resulting change in ground space. ([arXiv][5])

**Why it matters.** These connections clarify both originality and mechanism. The models are not unrelated new Hamiltonians; the potentially new results concern particular components, parameter regimes and quantitative gap statements. Conversely, one cannot transfer the full Motzkin gap theorem to a component after changing its kernel.

**Required revision.** Add a compact comparison identifying local forbidden vectors, interaction rank, normalisation, boundary conditions, ground-space structure and the exact gap statement supplied by each source. Retain the distinction between “this component already appeared” and “this theorem was already proved”. I did not establish the latter for the manuscript’s full opposing-bias result.

## 5. Rigour, results and inference

### Local spectra and the marker construction

The overlap calculation in Lemma 3.1 and the reducing subspace in Theorem 3.2 appear correct. The marker basis remains orthogonal even when \(u\) and \(v\) are not orthogonal, because the distinguished vector \(w\) occupies different sites and is orthogonal to both.

The restricted Hamiltonian produces the tridiagonal matrix with eigenvalues

$$
1-2ab\cos(k\pi/N),\qquad 1\le k\le N-1.
$$

The matching global lower bound makes the lowest value the **full-chain gap**, rather than merely an excitation energy in a convenient sector.

The local-spectrum multiplicities pass simple consistency checks:

$$
21+1+4+1=27,
$$

and

$$
\operatorname{tr}H_3
=\frac12+4+\frac32=6,
$$

as required for the sum of two rank-three embedded projectors.

### Dimer decomposition and the uniform bound

Theorem 4.1 identifies frozen unmatched symbols and decomposes the remaining degrees of freedom into monomer–dimer intervals. The connectivity argument is essential: it identifies the complete connected sectors, rather than selecting a favourable subset.

The similarity transform to hard-core heat-bath dynamics is consistent with

$$
p=a^2,\qquad d=b^2,\qquad p+d=1.
$$

The block-coupling argument gives a block-dynamics gap of at least \(2d\). The Dirichlet-form comparison then yields

$$
\operatorname{gap}(L)\ge d^2=b^4.
$$

At the balanced point, this becomes \(1/4\), as claimed.

I found no missing factor proportional to chain length in the continuous-time normalisation. Such a factor would destroy the uniform conclusion, so this is a consequential check. The endpoint product constraints are also treated separately; the deterioration of the bound as \(b\to0\) does not contradict their gap of one.

### Four-site certificate and perturbation stability

The rational positive-semidefinite certificate in §6.2 checks exactly. The five-state block and its factorisation support

$$
\gamma_4(P_{\mathrm d})\ge\frac25.
$$

The component count provides another sanity check:

$$
36(1)+14(2)+4(3)+1(5)=81.
$$

Each connected component contributes one zero mode, giving

$$
36+14+4+1=55
$$

zero modes and rank \(81-55=26\).

The decisive step is §6.3. For arbitrary rank-one qutrit projectors,

$$
\operatorname{rank}H_2\le1,\quad
\operatorname{rank}H_3\le6,\quad
\operatorname{rank}H_4\le26.
$$

The dimer model attains these maxima. Consequently, once Weyl’s inequality keeps the existing positive eigenvalues positive, additional positive eigenvalues cannot emerge from the kernel without exceeding the rank bounds. This addresses a genuine danger in perturbing highly degenerate frustration-free Hamiltonians.

The constants then follow correctly:

$$
\frac{3(2/5)-1}{2}=\frac1{10},
$$

and

$$
\frac{3(2/5-3\epsilon)-1}{2}
=\frac1{10}-\frac92\epsilon.
$$

At \(\epsilon=1/90\), the certified gap is \(1/20\).

The full-Schmidt-rank example also passes:

$$
\|P_*-P_{\mathrm d}\|^2=\frac1{13468}<\frac1{8100},
\qquad
\gamma_3(P_*)=\frac{10001}{20202}<\frac12.
$$

It therefore genuinely demonstrates a four-site certificate succeeding beyond the stated elementary three-site test.

### Rank-two bottleneck

The one-vacancy subspace is reducing because particle species cannot exchange order. Its positive kernel vector satisfies

$$
g_j=\prod_{i=1}^{j}q_{\sigma_i}.
$$

The trial vector is orthogonal to this kernel vector and hence to the entire ground space after embedding the reducing sector into the full Hilbert space. The variational argument is therefore legitimate despite the substantial global degeneracy.

The Rayleigh quotient

$$
\frac{a^{2k}}{1+a^2}
\left(\frac1{W_L}+\frac1{W_R}\right)
$$

has the stated interpretation: two regions with substantial ground-state weight are separated by a small amplitude.

For \(a=1/2\), \(b=2\),

$$
A=B=\log2,\qquad
\frac{2AB}{A+B}=\log2.
$$

At \(N=2L+1\), the exponential factor is

$$
e^{-(\log2)(2L)}=4^{-L},
$$

consistent with the specialised bound.

The argument proves an upper bound. It does not establish that the exponent is optimal, that the constructed sector determines the full gap asymptotically, or that the gap cannot decay faster.

### Reproducibility

| Check                                      | Result                                                   |
| ------------------------------------------ | -------------------------------------------------------- |
| Submitted exact verifier                   | All 27 check groups passed                               |
| Submitted sector enumeration               | All 9,840 words at lengths 1–8 passed                    |
| Submitted numerical regression             | All 35 cases passed                                      |
| Independent direct word-basis Hamiltonians | 20 cases passed                                          |
| Independent complex perturbations          | 18 short-chain tests passed                              |
| Independent hard-core heat-bath systems    | 50 finite systems passed                                 |
| Additional opposing-bias trials            | 24 exact orthogonality and energy-identity checks passed |

The exponential expressions in the last group were additionally evaluated numerically; that portion is diagnostic rather than exact symbolic verification.

The independent full-matrix calculation reproduced, at \(N=6\), approximately \(0.1339745962\) for the marker, \(0.3535563605\) for the dimer and \(0.0202041029\) for the opposing-bias example.

**Overall mathematical assessment:** the supplied proofs support the stated bounded conclusions. The finite computations corroborate them and expose reproducible certificates; they do not substitute for the all-length arguments.

## 6. External literature check

**Review date:** 28 September 2026. I used live web search and Exa to locate primary material, then consulted arXiv or publisher full texts and publication records. Searches included “rank-one qutrit frustration-free spectral gap”, “locally isospectral gapped gapless chains”, the explicit dimer and marker terms, “non-interacting Motzkin chain”, and opposing-bias hopping models. I included older papers where their exact Hamiltonians or classification theorems were decisive.

The external inspection concentrated on relevant definitions and theorem statements. It was not a complete re-refereeing of every external proof, nor an exhaustive bibliographic search.

The main findings are:

**The qubit baseline materially changes positioning.** Bravyi–Gosset supply the classification used in the independent comparison above. Their treatment also places the familiar biased hopping gap formula in established context. ([arXiv][1])

**The deterministic-certification discussion is substantially accurate.** Lemm already provides deterministic overlap criteria and neighbourhood statements. Hunter-Jones and Lemm address bounded-degree graphs, including large-local-dimension regimes; this is not a completed deterministic qutrit classification. ([arXiv][2])

**The manuscript correctly limits its relationship to the semidefinite hierarchy.** Rai and colleagues construct a systematic hierarchy containing established finite-size certificates. The present paper does not implement that hierarchy or demonstrate improved general performance. The journal record confirms the cited 2026 publication. ([arXiv][6])

**The PVBS distinction is legitimate.** Bishop’s two-species Product Vacua and Boundary States model contains additional interactions and has a different ground-space structure. Its conclusion about adding species does not contradict the manuscript’s hopping-only example. ([arXiv][7])

**The important omissions are structural antecedents.** The Motzkin comparisons in Comment 4.2 should be added. Movassagh and colleagues also provide earlier context for unfrustrated low-rank qudit chains and product ground states, relevant to Lemma 1.1. ([arXiv][8])

The search did not establish prior publication of the particular flat-Schmidt qutrit separation. That remaining uncertainty should be stated without treating an unsuccessful search as proof of novelty.

## 7. Minor comments

1. **Use “exponential gap upper bound” where precision matters.** The title of Theorem 2.3 and the release summary currently invite a stronger asymptotic reading than the proof establishes.

2. **Distinguish two meanings of an open region.** Theorem 2.2 concerns an open neighbourhood in the full rank-one projector space. The opposing-bias region is open within the specified two-parameter hopping family. Stability under arbitrary nearby rank-two projectors has not been shown.

3. **Make quantitative and terminological boundaries easier to find.** An explicit sufficient size threshold can replace “sufficiently large \(N\)” in Theorem 2.3; for the two-block construction, \(N\ge2+\lceil B/A\rceil\) suffices. Also clarify near the title or first theorem that “locally isospectral” means the specified two- and three-site spectra, and that “phase” refers to the paper’s open-chain gap classification.

## 8. Prioritised revision plan

**Must fix before publication.** Revise the contribution statement around the flat-Schmidt, genuinely qutrit separation. Include the qubit corollary or an equivalent comparison. Add the explicit Motzkin/free-Motzkin relationships, reconciling normalisation, boundaries and omitted terms. Update the abstract, introduction and release summary consistently.

**Should fix to strengthen the paper.** Add the dimension-minimality corollary for flat rank-two Schmidt data. Promote the short-chain rank-maximality argument into a clearly labelled lemma, since it is central to the perturbation theorem. Provide a concise result-by-result account of what is established prior work, what is a specialised consequence and what remains a candidate new contribution.

**Could improve future research.** A classification of the isospectral interpolation, or a general theorem identifying when local spectral data fail to determine gap behaviour, would broaden the contribution. A matching lower bound for the rank-two bottleneck could also sharpen that result. These are research extensions, not prerequisites for publishing the present bounded theorems.

## 9. Editorial recommendation

**Major revisions.**

The reasons are substantive contribution positioning and missing direct comparisons, rather than an identified failure of the principal proofs. The manuscript’s explicit acknowledgement that priority is unconfirmed is appropriate, but a publishable account still needs to explain its closest mathematical antecedents.

My confidence is **high in the reproduced finite calculations**, **moderately high in the central analytic arguments**, and **moderate in the originality assessment**.

A revision addressing the two major comments could make a credible specialist paper without solving the entire qutrit classification problem. Discovery of a prior theorem reproducing the flat-Schmidt separation or the full quantitative opposing-bias result could lower that assessment. A successful specialist comparison establishing a substantive distinction would strengthen it.

## 10. Provisional REF calibration

The most natural placement is **Unit of Assessment 10, Mathematical Sciences**, with Physics as a possible alternative depending on the submission context. Both remain within Main Panel B. ([REF 2029][9])

I checked the current REF 2029 material. The official timetable consulted schedules final panel criteria for autumn 2026; I did not locate a final Mathematical Sciences rubric during this review. I therefore use the published generic star definitions, distinguishing internationally excellent work at 3* from world-leading work at 4*, without inventing panel-specific weights. ([REF 2029][10])

| Dimension                  |   Indicative rating | Rationale and confidence                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | ------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Originality**            |              **3*** | The flat-Schmidt qutrit separation, its construction and the explicit certificates plausibly provide a substantive original contribution. The broader obstruction is readily obtainable from prior qubit theory, and the Motzkin antecedents require fuller comparison. **Moderate confidence.**                                                          |
| **Significance**           |              **2*** | Useful examples, quantitative bounds and clarification of the limits of particular spectral data. The paper has not yet established a broadly applicable classification principle or demonstrated a comparably substantial change in the field’s methods. **Moderate confidence.**                                                                        |
| **Rigour**                 | **4***, provisional | The strongest dimension: analytic all-length arguments, correct treatment of degeneracy, exact positive-semidefinite certificates, reproducible code and clear separation of proof from numerics. This is a judgement about the work inspected, not formal certification. **Moderate confidence in the grade; stronger confidence in the finite checks.** |
| **Overall output quality** |              **3*** | A coherent and technically credible specialist contribution, with originality and significance insufficiently established for 4*. **Moderate confidence, with a material 2*/3* boundary risk.**                                                                                                                                                           |

The overall rating is holistic, not the arithmetic mean of these diagnostic scores. It is an indicative assessment of research quality, not an official panel decision or a finding about submission eligibility.

**The main obstacle to 4* is the extent of the established new contribution.** Additional polishing or larger numerical runs would not resolve that issue. The proposed revision should first make the strongest existing theorem unmistakable; a higher rating would then depend on its demonstrated significance relative to the closest prior results.

## 11. References

### Classification, low-rank chains and gap certification

Bravyi, S., & Gosset, D. (2015). Gapped and gapless phases of frustration-free spin-\(1/2\) chains. *Journal of Mathematical Physics, 56*, 061902. [https://arxiv.org/abs/1503.04035](https://arxiv.org/abs/1503.04035)

Hunter-Jones, N., & Lemm, M. (2025). *Two classes of quantum spin systems that are gapped on any bounded-degree graph* [Preprint]. arXiv. [https://arxiv.org/abs/2509.22438](https://arxiv.org/abs/2509.22438)

Lemm, M. (2019). Gaplessness is not generic for translation-invariant spin chains. *Physical Review B, 100*, 035113. [https://doi.org/10.1103/PhysRevB.100.035113](https://doi.org/10.1103/PhysRevB.100.035113)

Movassagh, R., Farhi, E., Goldstone, J., Nagaj, D., Osborne, T. J., & Shor, P. W. (2010). Unfrustrated qudit chains and their ground states. *Physical Review A, 82*, 012318. [https://arxiv.org/abs/1001.1006](https://arxiv.org/abs/1001.1006)

Rai, K. S., Kull, I., Emonts, P., Tura, J., Schuch, N., & Baccari, F. (2026). A hierarchy of spectral gap certificates for frustration-free spin systems. *Quantum, 10*, 2065. [https://doi.org/10.22331/q-2026-04-13-2065](https://doi.org/10.22331/q-2026-04-13-2065)

### Motzkin and two-species comparisons

Andrei, R., Lemm, M., & Movassagh, R. (2022). *The spin-one Motzkin chain is gapped for any area weight \(t<1\)* [Preprint]. arXiv. [https://arxiv.org/abs/2204.04517](https://arxiv.org/abs/2204.04517)

Bishop, M. R. (2017). *Spectral gaps for the two-species Product Vacua and Boundary States models on the \(d\)-dimensional lattice* [Preprint]. arXiv. [https://arxiv.org/abs/1705.04755](https://arxiv.org/abs/1705.04755)

Bravyi, S., Caha, L., Movassagh, R., Nagaj, D., & Shor, P. W. (2012). Criticality without frustration for quantum spin-1 chains. *Physical Review Letters, 109*, 207202. [https://doi.org/10.1103/PhysRevLett.109.207202](https://doi.org/10.1103/PhysRevLett.109.207202)

Salberger, O., Padmanabhan, P., & Korepin, V. (2018). *Non-interacting Motzkin chain—Periodic boundary conditions* [Preprint]. arXiv. [https://arxiv.org/abs/1809.00709](https://arxiv.org/abs/1809.00709)

### REF assessment framework

Research Excellence Framework. (n.d.-a). *Guidance on REF 2021 results*. Retrieved September 28, 2026, from [https://2021.ref.ac.uk/guidance-on-results/guidance-on-ref-2021-results/index.html](https://2021.ref.ac.uk/guidance-on-results/guidance-on-ref-2021-results/index.html)

Research Excellence Framework. (n.d.-b). *Timetable: REF 2029*. Retrieved September 28, 2026, from [https://2029.ref.ac.uk/about/timetable/](https://2029.ref.ac.uk/about/timetable/)

Research Excellence Framework. (n.d.-c). *Units of assessment: REF 2029*. Retrieved September 28, 2026, from [https://2029.ref.ac.uk/panels/units-of-assessment/](https://2029.ref.ac.uk/panels/units-of-assessment/)

[1]: https://arxiv.org/pdf/1503.04035 "https://arxiv.org/pdf/1503.04035"
[2]: https://arxiv.org/html/1903.00108v2 "Gaplessness is not generic for translation-invariant spin chains"
[3]: https://www.quantum.physics.sk/rcqi/research/publications/2012/rcqi2012caha_PhysRevLett.109.207202.pdf "https://www.quantum.physics.sk/rcqi/research/publications/2012/rcqi2012caha_PhysRevLett.109.207202.pdf"
[4]: https://arxiv.org/pdf/1809.00709 "https://arxiv.org/pdf/1809.00709"
[5]: https://arxiv.org/html/2204.04517 "https://arxiv.org/html/2204.04517"
[6]: https://arxiv.org/html/2411.03680v3 "https://arxiv.org/html/2411.03680v3"
[7]: https://arxiv.org/pdf/1705.04755 "https://arxiv.org/pdf/1705.04755"
[8]: https://arxiv.org/abs/1001.1006 "https://arxiv.org/abs/1001.1006"
[9]: https://2029.ref.ac.uk/panels/units-of-assessment/ "https://2029.ref.ac.uk/panels/units-of-assessment/"
[10]: https://2029.ref.ac.uk/about/timetable/ "https://2029.ref.ac.uk/about/timetable/"
