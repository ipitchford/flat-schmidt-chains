# AI research index: flat Schmidt-rank-two chains

## Identity and status

Anonymous, *A spectral-gap classification for flat Schmidt-rank-two chains*, v1.0.1-candidate, 28 September 2026. DOI: [10.5281/zenodo.23024569](https://doi.org/10.5281/zenodo.23024569). Concept DOI: [10.5281/zenodo.23024568](https://doi.org/10.5281/zenodo.23024568). [Repository](https://github.com/ipitchford/flat-schmidt-chains), immutable tag `v1.0.1-candidate`.

Unrefereed written proof candidate with finite producer checks. Not a formal proof, authenticated independent reproduction, novelty clearance or official REF assessment. Read [status](STATUS.md), [provenance](PROVENANCE.md) and [review response](REVISION_RESPONSE_V101.md).

## Exact claim and scope

For every finite local dimension d >= 2, a homogeneous open nearest-neighbour chain H_N=sum_i |psi><psi|_(i,i+1), N >= 2, with a normalised forbidden vector of Schmidt probabilities (1/2,1/2,0,...), is gapless precisely when psi=(u tensor w - w tensor v)/sqrt(2) up to phase, with unit u,v,w and w perpendicular to u,v. Every such gapless chain has gamma_N=1-cos(pi/N). All other interactions in this class are uniformly gapped. Local projector rank is ONE; forbidden-vector Schmidt rank is TWO.

For an intersection line Cw, t is the nontrivial principal-angle cosine and tau=2|<w,w|psi>|^2. If tau>0, gamma_N >= 3 tau (2-t)(1-t)/1024. Coincident supports are gapless; disjoint supports have gamma_N >= 1-||Pi_L Pi_R||.

The qutrit family psi_theta=(cos(theta)|00>+sin(theta)|01>-|12>)/sqrt(2), 0<=theta<=pi/2, is the complete specified short-spectrum fibre. Its gap is >=cos(theta)^2/6 before the endpoint and exactly 1-cos(pi/N) at the endpoint. Schmidt probabilities, H_2/H_3 spectra and D_N=F_(2N+2) agree throughout. Full spectra at larger lengths are NOT asserted to agree.

## Claims, proof locations and trust boundary

| Claim | Location | Evidence boundary |
|---|---|---|
| Flat Schmidt dichotomy | [TeX](paper/flat_schmidt_chains.tex), `thm:classification` | Universal analytic argument, not proved by finite spectra |
| Exact marker gap | `thm:marker` | Lower bound plus matching reducing sector |
| Saturation obstruction | `lem:quantitative`, `lem:saturation` | Complex contractions and clipped open-boundary windows |
| Fibre classification | `thm:fibre`, `lem:gram`, `app:basis` | Normal form and full range-Gram block decomposition; negative direction killed by C |
| Constant degeneracy | `prop:degeneracy` | All-parameter rewriting proof; recurrence has earlier antecedents |
| Dimer/stability extensions | `thm:dimer`, `thm:ball` | Sufficient lower bounds, not general classification |
| Opposing-bias model | `thm:ranktwo-main` | Exponential UPPER bound only, no matching asymptotic lower bound |

## Reproduce and falsify

Install [pinned requirements](requirements-recorded.txt) in Python 3.13, then run [manifest verifier](code/verify_manifest.py) before [reproduce.sh](reproduce.sh). Replay writes new timing/report files; do so in a disposable extraction. Run `python code/publication_controls.py` and `python -OO code/publication_controls.py`. The controls deliberately remove the symbolic guard and require the classifier regression suite to reject the mutant.

The [classifier](code/classify_flat.py) accepts parameter-free exact SymPy matrices only. Free symbols and floats are rejected; specialise first. For the reviewer family M(x), x=0 is gapless and x=1 uniformly gapped. Generic symbolic ranks must not be used as universal phase certificates.

[Exact certificates](evidence/classification_certificates.json), [exact report](evidence/classification_exact.json), [numerical report](evidence/classification_numerics.json), [classifier tests](evidence/classifier_tests.json). Finite tests do not establish every parameter/length. The manuscript's global-versus-sector argument and range restriction are load-bearing.

## Dependencies, prior art and open work

See [source audit](sources/SOURCE_AUDIT.md) and [intake citation audit](CITATION_AUDIT.md). Bravyi–Gosset supplies the qubit predecessor; overlap methods, the ground-space recurrence and unbiased hopping gap have established antecedents. No exhaustive priority claim.

Unequal Schmidt probabilities, arbitrary rank-two projectors, periodic/GNS gaps, matching opposing-bias asymptotics, and universality of the saturation mechanism outside this class remain open here. Request unaffiliated checking of the saturation inequality and normal-form completeness before high-assurance reuse.

## Rights

[Licence map](LICENSES.md): original prose/data CC0-1.0; original code MIT. Preserved third-party material retains upstream terms. Do not infer independent validation or human research authorship from the publisher or this index.
