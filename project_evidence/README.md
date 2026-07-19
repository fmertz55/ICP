# Project evidence — separate evidentiary tier

This directory contains audits, derived data, and preregistrations based on ICP,
PSA, IOTA, or AIidea project artifacts. These materials are **not independent
literature evidence** and are never counted in the source totals under
`library/source_index.csv`.

The separation prevents three errors:

1. using project-generated results to validate the framework that motivated
   them;
2. mixing an engineering pipeline artifact with a peer-reviewed field result;
3. letting exploratory inspection silently become confirmatory evidence.

Current records:

- `psa_zipf_data_audit.md` — provenance and censoring audit (`PZ-A001`);
- `reconstruct_psa_l1_occupancy.rb` — deterministic common-resolution repair;
- `psa_run2_common_l1_occupancy.csv` — derived Run-2 L1 occupancy table;
- `psa_anchor_winner_audit.py` — read-only reproducibility check for the
  exploratory 115-star tokenization;
- `psa_zipf_preregistration.md` — bounded sequence and intervention design
  (`PZ-P001`).

Project evidence may motivate a test of ICP, expose a failure mode, or supply an
empirical case. It cannot by itself establish the larger ICP grounding.
