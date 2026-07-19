# Pilot Batch 02 — Zipf as an adversarial test of causal underdetermination

- Date: 2026-07-19
- Protocol: 0.3
- Scope: Zipf mechanisms, power-law inference, type-token dynamics, and a
  bounded PSA feasibility audit
- Independent literature base: 19 peer-reviewed sources (`S020`–`S038`)
- Project evidence: separately tiered and not counted as independent support
- Status: mechanism-discrimination pilot, not a universal review of scaling
  laws and not a confirmatory analysis of PSA

## Outcome first

Zipf is valuable to ICP for the opposite of the usual reason. A straight
rank-frequency curve is compatible with mutually incompatible causes:

- independent random characters or fixed categorical sampling;
- cumulative advantage and innovation;
- speaker-hearer optimization;
- broad latent-variable mixtures;
- critical-like probability landscapes;
- maximum-entropy inference under selected constraints;
- history-dependent sample-space reduction;
- finite-size, aggregation, censoring, and transient undersampling.

The marginal therefore does **not** evidence memory, semantic organization,
counterfactual restriction, a physical carrier, criticality, or ICP. Simon
already made the central warning in 1955: fitting the skew distribution tells
little about the underlying phenomenon when multiple mechanisms produce it.
Li's random-text construction supplies a memory-free counterexample; Schwab et
al. supply a latent-mixture counterexample; Corominas-Murtra et al. supply a
genuinely history-dependent construction. The same visual law spans all three.

The defensible ICP question is instead:

> Among histories with the same present marginal counts, which proposed record
> or organization predicts the intervention-sensitive law of future reuse,
> novelty, or reachable successors—and does manipulating its physical carrier
> change that law?

This turns Zipf from supporting iconography into a falsifiable laboratory.

## Three statistical objects that must not be conflated

Let `c(r)` be the count of the type at rank `r`, `C` the count of a randomly
selected type, `N` the number of observed tokens, and `V(N)` the number of
distinct types. Then three different claims are:

`c(r) proportional to r^(-a)` — rank-count or rank-size law;

`P(C = n) proportional to n^(-gamma)` — distribution of type counts;

`V(N) proportional to N^beta` — Heaps or type-token growth.

For finite discrete systems the first two formulations are not exactly
equivalent. The familiar `gamma = 1 + 1/a` relation is asymptotic and can be
misleading when fitted to empirical ranks. The third object is a temporal path,
not a final marginal. A final frequency multiset does not select a unique
`V(N)` trajectory.

Rosillo-Rodes et al. derive a precise type-token relation for an idealized
deterministic system that maintains a prescribed inverse-power ranking. Near
`a = 1`, logarithmic corrections matter; the mechanical `beta = 1/a`
conversion is not valid. Zimmerlin et al. go further: holding the final count
multiset fixed, token reorderings can generate a range of discovery paths,
including accelerated and delayed envelopes. The observed order effect is
domain dependent—small in their tested Gutenberg texts and large in music
listening and web browsing.

Consequently, Heaps scaling is not a second independent vote for ICP. Its
information lies in the temporal path after the final counts have been held
fixed.

## Mechanisms and discriminating predictions

The full adversarial matrix is in
`analysis/zipf_mechanism_matrix.csv`. Its central comparisons are:

| Candidate | Proposed state or cause | Prediction beyond the slope | Decisive control |
|---|---|---|---|
| Random typing / IID | fixed character or type probabilities | geometric lengths, plateaus, no history-conditioned next-event gain | simulate at observed size; within-document shuffle |
| Yule-Simon | accumulated counts plus innovation rule | reinforcement, age effects, linked innovation and vocabulary growth | count equalization and innovation intervention |
| Least effort | signal-referent association matrix and cost weight | mutual information, ambiguity, and lexicon size move jointly | manipulate or stratify communicative costs |
| Latent mixture | topic, stimulus, part of speech, or other common input | pooled Zipf weakens under conditioning | hierarchical and preregistered latent conditioning |
| Criticality | interaction network and operating point | finite-size scaling, susceptibility, response to coupling perturbation | vary size and couplings after controlling common drive |
| Maximum entropy | selected expectation constraints | exponent or cutoff follows declared constraint; no native path signature | identify and manipulate a physical enforcement mechanism |
| Sample-space reduction | current state and nested reachable set | directional successor pruning, resets, reverse-time asymmetry | order shuffle, time reversal, support intervention |
| Dynamical coherence | evolving support, cutoffs, and population | coherent longitudinal parameter evolution | frozen prefixes and time slices |

No mechanism is accepted because its vocabulary sounds like ICP. Sample-space
reduction is the closest literal match to counterfactual future-state
restriction, but its downward order, reset, and nested support are assumptions
to be tested. A static grammar, topic hierarchy, or network topology can mimic
the same transition asymmetry without a distinct historical carrier.

## The ICP mapping

For event sequence `X_1, X_2, ...`, let history `H_t` be compressed into a
candidate present state `M_t = phi(H_t)`. Let `pi` index an admissible analytic
or physical intervention, and let

`Q^pi_tau(. | M_t, A, B)`

denote the law of the next event or future path at horizon `tau`, relative to
observable set `A` and boundary/resource declaration `B`.

A final count vector `C_t` is one possible state summary. The mechanism test
compares histories `h` and `h'` for which `C_t(h) = C_t(h')` but other
organization differs. The minimal empirical question is whether

`Q^pi_tau(. | h) = Q^pi_tau(. | h')`

to a preregistered tolerance. If equality holds, the extra history has not
constrained the declared future beyond counts. If it fails out of sample, then
history-sensitive organization exists at the stated representation. That still
does not establish physical embodiment.

The stronger ICP sequence is:

1. **Formation:** different controlled histories form different candidate
   states.
2. **Conditional sufficiency:** systems matched on `M_t` have the same future
   law within tolerance.
3. **Sequential discrimination:** at least one pair of `M_t` values predicts
   different future laws beyond the marginal.
4. **Rival defeat:** the effect survives IID, latent-mixture, grammar/topology,
   finite-size, and preprocessing alternatives.
5. **Carrier intervention:** perturbing, erasing, or replacing the proposed
   physical realization changes the future law as predicted.
6. **Representation declaration:** dependence on tokenizer, boundary, scale,
   and intervention family is either controlled or made part of the result.

A shuffle is an analytic intervention on sequence organization, not a physical
counterfactual for the same material system. It establishes path sensitivity;
only a structural model or carrier manipulation can support stronger causal or
counterfactual language.

## Statistical gate before mechanism inference

Clauset, Shalizi, and Newman remain the primary gatekeeper for a power-law
existence claim, qualified by Corral et al. for discrete Zipf representations
and by the dependence structure of text and prefixes.

The preregistered sequence is:

1. Freeze corpus, independent unit, token and type definitions, document
   boundaries, case and punctuation rules, deduplication, aggregation, and the
   exact Zipf formulation.
2. State whether the claim is exact exponent one, free exponent, whole domain,
   or tail only.
3. Use likelihood-based estimation for the declared discrete object. A rank
   plot and `R^2` are descriptive diagnostics only.
4. Estimate or model the lower cutoff and propagate its uncertainty. Report the
   number and fraction of independent units retained.
5. Bootstrap absolute goodness of fit while refitting all selected parameters.
   Non-rejection means “not rejected,” not “verified.”
6. Compare the same support against discrete lognormal, stretched exponential,
   cutoff power law, Yule-Simon, Zipf-Mandelbrot or double-power alternatives,
   and mechanistic models appropriate to the domain.
7. Calibrate dependence at the document or temporal-block level. Ordinary
   token-level or pair-level IID uncertainty is not valid.
8. For type-token dynamics compare original order, within-sequence shuffle, and
   block shuffle; report local slope and curvature rather than only one global
   Heaps exponent.
9. Repeat across a frozen preprocessing multiverse and an independent corpus.

Recommended result labels are:

- **Rejected:** absolute goodness of fit fails.
- **Inconclusive:** too little information or inadequate discrimination power.
- **Plausible but nonunique:** not rejected, but competitors remain.
- **Supported on the stated range:** absolute fit, rival comparison, dependence
  calibration, and replication pass.
- **Descriptive Zipf-like scaling:** visual or regression evidence only.

Even “supported on the stated range” supports a distribution, not ICP. The
mechanism and carrier gates remain.

## PSA feasibility audit: the first useful failure

The separate project audit found that the obvious PSA voxel analysis is
invalid. In the April Run-2 snapshot:

- 3,378 sentences occupy 674 stored adaptive cells;
- the maximum stored count is exactly 21;
- 51 cells contain exactly 21 sentences;
- 229 cells are singletons.

This is mechanical. The adaptive router computes approximately

`heat = log(sentence_count) * (1 + variance)`

and subdivides when heat reaches 3. With small variance, `log(20) < 3` and
`log(21) > 3`. Subdivision occurs after the twenty-first insertion; existing
sentences remain in the parent and later arrivals enter descendants. A
rank-frequency analysis over mixed L1 and L2 labels therefore measures the
routing threshold and ingestion history as much as the semantic field.

Mapping every `L_l_v_x_y_z` to its L1 ancestor,

`(floor(x / 2^(l-1)), floor(y / 2^(l-1)), floor(z / 2^(l-1)))`,

and summing parent plus descendant mass reconstructs 417 common-L1 cells whose
counts total all 3,378 sentences. Their leading counts are 61, 61, 60, 59, and
55 rather than a capped 21. This repair makes a marginal-only exploratory
analysis possible. It does not recover the event path or make the marginal
mechanistically identifying.

The current cross-model corpus is better for sequence work. It contains 3,304
SentenceNodes in 11 documents, each with a complete unique sentence index from
zero to its final position. Document lengths range from 38 to 677. A
tier-weighted 115-anchor winner representation uses 91 of 115 anchor categories
and is large enough for a bounded sequence analysis. Because these marginals
were inspected during feasibility work, any fit on them is exploratory; a
confirmatory claim requires frozen future documents.

The April Run-1 and Run-2 experiments are not clean same-endpoint order
randomizations: they end with 3,349 and 3,378 SentenceNodes, respectively, and
the stored artifacts do not contain the full per-sentence assignment path.
Replaying their document orders on the current corpus would be an offline
counterfactual emulation, not a replication.

Full audit, file provenance, and the reconstruction script are in
`project_evidence/`.

## Bounded PSA experiment

The preregistered primary representation is the tier-weighted winning anchor
from the 115-star catalog, with 75-star, disjoint 58/57-star, random-anchor, and
train-fold-calibrated grids as sensitivity analyses. Adaptive mixed-resolution
labels are prohibited as the primary marginal.

The experiment preserves every document boundary and natural sentence order.
Its primary null uses 1,000 within-document permutations, which preserve every
document and global frequency marginal exactly. Block shuffles of 5 and 20
sentences diagnose scale; document-order permutations apply only to cumulative
inventory questions.

The primary outcome is leave-one-document-out prequential log-loss gain of an
order-aware transition model over a document-conditioned IID marginal. A
conditional-mutual-information permutation statistic is secondary. Innovation
outcomes include `K(t)`, first-arrival times, and the probability that the next
token is new, compared against finite IID, Pólya/Yule-Simon, Pitman-Yor, and
finite-order transition models.

The direct ICP sufficiency comparison is nested:

- `M0`: counts and document/time exposure only;
- `M1`: `M0` plus current anchor token;
- `M2`: `M1` plus richer recent history;
- `M3`: `M2` plus source/topic covariates.

If `M2` supplies no reproducible held-out gain over `M0`/`M1`, or performs like
within-document shuffles, the sequence-bearing ICP claim fails for this
representation. If source/topic covariates absorb the gain, the latent-mixture
account is preferred. Even if a robust gain remains, the conclusion is
history-sensitive semantic organization—not yet a physically embodied ICP
carrier.

Catalog replacement and routing-radius changes are representation or access
interventions. They can test robustness and reachable comparison sets. They do
not by themselves manipulate a physical memory carrier.

## Graded conclusions

### Established field results

- Several incompatible mechanisms generate Zipf-like marginals.
- Random typing demonstrates that no memory is required for a coarse slope,
  although tested random-text models fail to reproduce full language data.
- Latent mixtures can produce Zipf and critical-like signatures without
  intrinsic fine tuning.
- Sample-space reduction produces Zipf through explicit path-dependent support
  pruning.
- Rank-count, count-distribution, and type-token laws are distinct finite-data
  objects.
- The final count multiset does not determine its discovery path.
- Rigorous distributional claims require absolute fit and alternative-model
  comparison, not visual linearity.

### Supported ICP synthesis

- The useful ICP observable is a family of conditional future laws, not the
  Zipf exponent.
- Count-matched history and shuffle designs expose organization hidden by a
  static marginal.
- A strong ICP claim additionally requires latent conditioning, ordinary-model
  comparison, and carrier intervention.

### Rejected or qualified inferences

- A Zipf slope is not evidence for ICP.
- Heaps scaling is not independent confirmation without an ordering model.
- Sample-space-reduction language is not automatically a physical mechanism in
  the target system.
- A MaxEnt constraint is not automatically an embodied system constraint.
- Critical-like Zipf statistics do not identify intrinsic criticality.
- PSA mixed-resolution voxel counts cannot be fitted naively because adaptive
  subdivision censors them at 21.

## Consequence for the name

This batch strengthens the earlier naming recommendation: retain **ICP** as the
umbrella, but expand it as the **Information–Constraint Program**, not yet the
Information–Constraint Principle. Zipf is an exemplary program test because it
can defeat the weak claim while sharpening a stronger operational one.

The paper-level technical claim should be narrower: **matched-marginal
future-law discrimination**. It asks whether an identified present state adds
out-of-sample prediction of future events under declared interventions after
counts, latent mixtures, and representation artifacts have been controlled.
That is defensible, falsifiable, and continuous with the formal core from Pilot
Batch 01.
