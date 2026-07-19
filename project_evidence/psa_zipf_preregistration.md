# PZ-P001 — PSA matched-marginal future-law discrimination

- Version: 0.1
- Drafted: 2026-07-19
- Status: analysis-ready exploratory preregistration; not yet executed
- Confirmatory status: none; future untouched documents must be frozen before
  any confirmatory claim
- Governing literature: `S020`–`S038`

## Scientific question

After document identity, exposure, and present marginal counts are controlled,
does the order and PSA organization of prior sentences improve out-of-sample
prediction of the next semantic token, novelty event, or reachable comparison
set?

This tests a narrow ICP proposition:

`history H_t -> proposed state M_t -> future law Q(X_(t+1) | M_t)`.

It does not test a universal Information–Constraint Principle, and it does not
identify a physical carrier unless a later carrier intervention is added.

## Hypotheses

### Primary null `H0-sequence`

Given document, position/exposure, and the accumulated token-count vector, the
natural order supplies no reproducible held-out information about the next PSA
token beyond an order-insensitive model. The observed statistic is exchangeable
with within-document permutations.

### Primary alternative `H1-sequence`

Natural order improves held-out next-token prediction beyond counts and lies in
the upper 5 percent of the within-document permutation distribution.

### Latent-mixture null `H0-mixture`

Any apparent sequence gain is absorbed by document/source, sentence position,
or preregistered topic covariates.

### SSR-specific alternative `H1-support`

The reachable successor set prunes directionally with history and predicts
held-out successors better than static grammar/topology and order-insensitive
baselines. Zipf-like occupancy alone is irrelevant to this test.

## Frozen data and independent unit

Primary corpus:

`/Volumes/douglasclark/aiidea/psa_test_runs/cross_model_transfer/corpus.jsonl`

SHA-256:

`4cf8970806cb5f3ef4cb9019d718736bd435cfe98872afcccfbe7159be5cade6`

The independent resampling and validation unit is the document, not the
sentence or sentence pair. Natural sequence never crosses a document boundary.
The 120 PromptSentence records in the larger embedding archive are excluded
from primary analysis.

## Token and type definitions

### Primary

Each sentence is assigned to the tier-weighted winning guide star in the frozen
115-star Qwen frame:

`token(e) = argmax_j w_j <e_hat, g_hat_j>`.

Sentence and anchor rows are independently L2-normalized. Zero-based anchors
69–74 have `w_j = 0.4`; all others have weight 1. Exact ties go to the lowest
index. The frozen sentence-archive and anchor hashes are recorded in PZ-A001,
and `psa_anchor_winner_audit.py` reproduces the exploratory occupancy summary.
Every execution must still record catalog ordering, runtime, and hashes in its
run manifest before the first model fit.

### Prespecified sensitivity representations

1. frozen 75-star Qwen catalog;
2. disjoint 58-star and 57-star subsets of the 115 catalog;
3. seed-frozen random sentence-anchor catalogs matched in size;
4. BGE-M3 and MPNet frame variants;
5. common-L1 reconstructed April Run-2 counts, marginal-only;
6. quantile grids fitted on training documents only at fixed resolutions.

Adaptive mixed-level voxel labels are prohibited as the primary marginal.
Existing full-corpus quantile calibration is prohibited for held-out tests.

## Splitting and leakage prevention

- Outer validation: leave one document out, producing 11 held-out folds.
- Hyperparameters and smoothing: chosen only within the 10 training documents
  of each outer fold by nested document-level validation.
- Vocabulary: training-fold catalog is fixed; an unseen held-out token maps to
  an explicit unknown/novel category where required.
- No sentence from a held-out document contributes to anchor fitting,
  calibration, topic estimation, smoothing selection, or cutoff selection.
- Marginal power-law fits on the already inspected corpus are labeled
  exploratory regardless of p-value.

## Surrogate interventions

### Primary shuffle

Generate 1,000 independent within-document permutations. Each permutation
preserves exactly:

- every document's length;
- every document's token-count multiset;
- the corpus-wide token-count multiset;
- all document labels.

It destroys natural successor order. A rank-frequency curve is therefore
identical by construction.

### Secondary shuffles

- permute blocks of 5 sentences within document;
- permute blocks of 20 sentences within document;
- permute document order only for cumulative-inventory analyses;
- reverse sentence order as an SSR directionality control.

These are analytic surrogates, not physical counterfactuals.

## Models

All models predict the same held-out next-token target and are evaluated on the
same positions.

1. `M0-document-IID`: document-conditioned or hierarchical categorical law
   without event order.
2. `M0-counts`: accumulated count vector, exposure, and novelty schedule but no
   last-token transition.
3. `M1-Markov`: `M0` plus current token and a regularized first-order transition
   law.
4. `M2-history`: `M1` plus prespecified recent-history summaries or finite
   context selected only inside training folds.
5. `M3-latent`: `M2` plus document/source, normalized position, and
   training-derived topic covariates.
6. Mechanistic comparators: finite IID, Pólya/Yule-Simon, Pitman-Yor, and an
   SSR/nested-support model where identifiable.

Model complexity is penalized through held-out log score, never training fit.
No model is favored because it is phrased in ICP language.

## Outcomes

### Primary

Leave-one-document-out prequential log-loss gain per held-out sentence:

`Delta = logloss(M0-document-IID) - logloss(M1-Markov)`.

Positive `Delta` favors order-aware prediction. The corpus-level statistic is a
document-size-weighted held-out sum; document-level gains are also reported so
one long document cannot hide heterogeneity.

### Secondary

- conditional mutual information between current and next token given
  document, position bin, and accumulated counts;
- `K_d(t)`, the distinct-token path within each document;
- first-arrival times and novelty hazard;
- successor-support size, nestedness, reverse-time asymmetry, and reset/run
  statistics;
- calibration, Brier score, and top-k next-token recall;
- De Marzo-style longitudinal coherence where the required cutoff model is
  adequate;
- marginal rank-count and count-distribution fits, explicitly exploratory.

## Decision rules

Evidence for sequence-sensitive organization requires all of:

1. observed primary `Delta > 0`;
2. observed `Delta` exceeds the 95th percentile of the 1,000 primary-shuffle
   statistics (`p_perm <= 0.05` with the plus-one correction);
3. document-level uncertainty is reported and the result is not driven solely
   by one document;
4. the sign and practical magnitude persist in at least the 75- and 115-star
   prespecified representations;
5. the gain survives an order-insensitive count/exposure comparator.

Evidence against the sequence-bearing version of ICP is recorded if the
primary rule fails, if shuffled order performs equivalently, or if the gain is
absorbed by `M3-latent` without a carrier-mediated residual.

SSR is supported only if reachable-support and directionality predictions pass
held-out tests against static transition, topic, and grammar/topology models.
A Zipf slope never contributes to that decision.

## Marginal power-law gate

For each declared representation, keep rank-count and type-count formulations
separate. Use discrete likelihood, estimated support/cutoff uncertainty,
refitted bootstrap goodness of fit, and same-support comparisons against
discrete lognormal, stretched exponential, cutoff power law, Yule-Simon, and
Zipf-Mandelbrot/double-power alternatives.

No claim is made when the effective tail has inadequate independent units or
simulation shows less than 80 percent power to distinguish the nearest
prespecified rival. Visual linearity is labeled descriptive.

## Access and intervention analysis

For train-fold-fitted quantile routing, vary radius over `{1, 6, 8, 11, 13}`.
At test sentence `t`, expose only inventory available before `t` and measure:

- fraction of prior inventory admitted to the candidate set;
- recovery of full-embedding nearest or high-similarity prior neighbors;
- held-out successor and retrieval performance;
- cost-recall frontier.

Catalog replacement and radius changes manipulate representation and access,
not the underlying sentence marginal. They test robustness and operational
reachable comparisons, not physical carrier causality.

## Interpretation ladder

- **No marginal fit:** no Zipf claim for that representation.
- **Marginal fit only:** descriptive scaling; no ICP evidence.
- **Order gain only:** history-sensitive statistical organization.
- **Order gain after latent controls:** stronger representation-level state
  evidence.
- **Mechanism-specific intervention success:** evidence for that mechanism at
  the declared scale.
- **Carrier manipulation with mediation:** first result eligible for embodied
  ICP language.

The current experiment can reach, at most, the fourth or fifth rung. It has no
authorized physical carrier intervention.

## Reproducibility outputs

Every execution must save:

- input and asset hashes;
- document manifest and exclusions;
- exact token assignments;
- fold and permutation seeds;
- preprocessing and model configuration;
- per-document predictions and scores;
- all failed and inconclusive outcomes;
- environment and code revision.

Outputs belong under the ICP project or a temporary directory. Existing AIidea
scripts with defaults that write into their source repository must not be
invoked for this analysis.
