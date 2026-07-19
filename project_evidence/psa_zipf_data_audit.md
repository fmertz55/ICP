# PZ-A001 — PSA Zipf data and architecture audit

- Audit date: 2026-07-19
- Evidence class: exploratory project evidence; not independent ICP support
- Mutation policy: AIidea artifacts read in place; no source-repository writes
- Primary conclusion: stored mixed-resolution voxel occupancies are
  mechanically right-censored and invalid for a naive Zipf fit

## Frozen inputs

### April Run-2 occupancy snapshot

Path:

`/Volumes/douglasclark/aiidea/psa_test_runs/run2_random_order/results/2026-04-17T171307Z_voxel_snapshot.json`

SHA-256:

`5aa805b068c0d61c2fc562d6a109ba0baf471ad5bf3d2f7cd277a12a527f125d`

The snapshot contains 3,378 assigned SentenceNodes across 674 stored adaptive
cells. The stored occupancy distribution has minimum 1, maximum 21, 51 cells at
exactly 21, and 229 singletons.

### Current sequence-bearing corpus

Path:

`/Volumes/douglasclark/aiidea/psa_test_runs/cross_model_transfer/corpus.jsonl`

SHA-256:

`4cf8970806cb5f3ef4cb9019d718736bd435cfe98872afcccfbe7159be5cade6`

The corpus contains 3,304 SentenceNodes in 11 documents. Each document has a
complete unique natural sentence index from zero to its final position, with no
gaps or duplicates; document lengths range from 38 to 677. Fields include
container, sentence identifier and text, a 4,096-dimensional embedding, coarse
and micro PSA labels, and paraphrase-group identifiers.

## Why the count 21 is architectural

The relevant implementation is:

`/Volumes/douglasclark/aiidea/app/consolidated_clustering_v2/routing/adaptive_grid.py`

The router updates heat as

`heat = log(sentence_count) * (1 + mean_cosine_variance)`

and subdivides a leaf when heat reaches the configured threshold 3. With small
variance:

- `ln(20) = 2.9957 < 3`;
- `ln(21) = 3.0445 > 3`.

Subdivision is checked after insertion. Existing parent members are retained
for reference and redistributed only lazily; future points are routed to child
cells. The resulting mixed-level table therefore has a predictable pile-up at
21. It is not an unconstrained tail sample.

This has two consequences:

1. a power-law fit to all stored L1/L2 labels is invalid;
2. the mixed-level representation encodes ingestion history by construction,
   so order sensitivity cannot be interpreted as semantic memory without
   controlling subdivision state.

## Common-L1 reconstruction

For a stored label `L_l_v_x_y_z`, the L1 ancestor is

`L1_v_floor(x / 2^(l-1))_floor(y / 2^(l-1))_floor(z / 2^(l-1))`.

Summing target-level and descendant mass reconstructs a common-resolution
marginal. The included script checks conservation of total sentence mass and
emits one row per L1 cell.

Run-2 result:

- 417 reconstructed L1 cells;
- total mass 3,378;
- maximum 61;
- top counts 61, 61, 60, 59, 55, 55, 50, 47, 47, 46;
- 47 reconstructed cells contain stored L2 descendants;
- only four cells remain exactly at 21 after aggregation rather than 51.

The output is `psa_run2_common_l1_occupancy.csv`. It is suitable for an
exploratory marginal analysis, subject to ordinary finite-sample and
representation gates. It contains no event ordering.

## Sequence feasibility

The current corpus supports exact within-document succession. Relevant frozen
assets include:

- `temp/psa_frame_overlap/v1_75_star_embeddings.npy`, shape 75 by 4,096;
- `temp/psa_frame_overlap/v2_115_star_embeddings.npy`, shape 115 by 4,096;
- `psa_test_runs/cross_model_transfer/frame_current_qwen3_115.npz`;
- BGE-M3 and MPNet frame/embedding archives in the same directory;
- `temp/psa_frame_overlap/neo4j_sentence_embeddings_3424_current.npz`, which
  contains the 3,304 SentenceNodes plus 120 PromptSentence records.

The exact exploratory token is

`argmax_j w_j <e_hat, g_hat_j>`,

where sentence and guide-star embeddings are independently L2-normalized,
`w_j = 0.4` for zero-based modality anchors 69–74, and `w_j = 1` otherwise.
An exact tie goes to the lowest index, following `numpy.argmax`. This matches
the tier weighting in `guide_stars.py` and signature construction in
`psa_cross_model_transfer.py`.

The sentence archive hash is
`1e880092edbfbde176fbce1197e87db7e06480172cf0b79bb82dc24081822c28`;
the 115-star array hash is
`89ee780fc3ce332544713e1471be5e6c44fcba7161302311c9526202b90b3c19`.
The read-only reproduction script is `psa_anchor_winner_audit.py`.

The check produced 91 occupied categories, maximum count 682, and 12 singleton
categories. This is sufficient for a bounded sequence comparison, but the
inspected marginal is no longer eligible for an untouched confirmatory
power-law claim.

## Data limitations and leakage controls

- April Run 1 and Run 2 are not the same endpoint: they contain 3,349 versus
  3,378 SentenceNodes. Their aggregate artifacts do not retain every
  per-sentence occupancy assignment through ingestion.
- Run 1's available locality result excludes singleton cells and is not a
  complete occupancy distribution.
- The July corpus differs from the April experiment, includes additional
  documents, and uses a newer version of one paper. Replaying April document
  order is an offline emulation, not replication.
- Wall-clock ingestion timestamps are absent. Natural sentence order is exact;
  ingestion timing is not.
- Existing 20-bin quantile calibration was fitted on all 3,424 records and
  leaks held-out ranks. Any confirmatory grid must fit calibration on training
  folds only.
- Pipeline-discovered paraphrase groups are selected and censored outcomes;
  they are secondary, not primary.
- Uncertainty must be document-level or permutation-based. Sentence pairs and
  nested prefixes are not independent replicates.

## Audit verdict

The architecture audit falsifies a naive mixed-voxel Zipf analysis before it is
run. That is a positive scientific result: the review's mechanism and
representation gates detected a pipeline-created regularity that a visual
rank plot would have mistaken for evidence.

The next admissible analysis is the bounded sequence design in
`psa_zipf_preregistration.md`, plus the common-L1 marginal as an explicitly
exploratory baseline.
