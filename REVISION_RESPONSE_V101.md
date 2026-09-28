# Version 1.0.1: response to the supplied 28 September review

The supplied review recommends minor revisions. Its identity and external independence have not been authenticated. Producer replay of its code is recorded separately, not called a new independent review. Main classification statements are unchanged.

| Item | Action and location | Disposition |
|---|---|---|
| 4.1 symbolic classifier | `code/classify_flat.py` rejects every free symbol before rank/null-space calculations. README and manuscript executable-domain paragraph specify parameter-free inputs. `code/test_classifier.py` adds the unspecialised family, x=0 (gapless, intersection dimension 2), x=1 (gapped, intersection dimension 1). `code/publication_controls.py` tests these under optimisation and requires a guard-removal mutation to fail. | Resolved |
| 4.2 antecedents | Contribution paragraph, ground-space proposition introduction, and Motzkin comparison cite Movassagh et al., Section II equation (11), and Bravyi et al., Step 1 before equation (6). Full-fibre persistence is distinguished from the inherited recurrence. | Resolved |
| 4.3 full Gram decomposition | Named Full range-Gram decomposition lemma and endpoint-safe symbolic basis appendix specify all 27 columns by tensor subspaces and exact orthogonalisation. Negative Gram direction is explicitly in ker C; no unrestricted positivity assertion. | Resolved |
| notation | Local meanings of c remain unchanged to avoid unnecessary proof transcription; section-specific definitions and the new basis appendix locate them. | Deliberate limitation |
| organisation | Main classification remains first; new contribution paragraph separates it from complementary results. Existing supplementary results retain their numbered sections, avoiding unnecessary renumbering of research cross-references. | Addressed within scope |
| exact bounds versus diagnostics | All public descriptions distinguish exact marker gap, uniform lower bounds, exponential upper bounds, and finite numerical corroboration. | Retained |
| broader saturation theorem | A result outside this Schmidt class would require new research. It is not claimed or made a publication condition. | Deliberate limitation |

The executable repair is not a counterexample to the theorem. The supplied review's prospective REF assessment is not an official rating and is not used as a public assurance badge.
