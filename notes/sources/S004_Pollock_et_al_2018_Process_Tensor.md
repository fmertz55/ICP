# S004 — Pollock et al. (2018), Non-Markovian Quantum Processes

## Bibliographic record

- Citation key: `PollockEtAl2018ProcessTensor`
- DOI: <https://doi.org/10.1103/PhysRevA.97.012127>
- Status: peer-reviewed theory and method
- Stratum: quantum process tensors and memory

## Why included

This is the closest formal match in the pilot to an operational family of
future laws indexed by interventions.

## Native result and formalism

The process tensor `T_(k:0)` maps a sequence of completely positive control
operations to the later system state. It is linear, completely positive, and
satisfies containment; it has system-environment dilations, a generalized Choi
representation, and a tomography procedure. Temporal correlations can be
represented in a matrix-product-operator form.

## Common-schema mapping

- `H`: prior system-environment evolution and applied controls.
- `M`: operational multi-time process; microscopic memory may reside in the
  environment.
- `Pi`: sequences of local CP maps at selected times.
- Future object: output density operator and probabilities of later instruments.
- Claim type: interventional-operational marginals, not a joint cross-world law.

## Assumptions, limitations, and rival reading

Completeness is relative to a system boundary, temporal grid, and control span.
A dilation need not be unique. Enlarging the state to include the environment
can remove reduced non-Markovianity, directly supporting rival `R002`.

## ICP relationship

- Direction/directness: supports / direct for the formal scaffold; qualifies /
  direct against irreducible-history claims.
- What ICP must add: a carrier identification and robustness criterion beyond
  the complete input-output description.

## Locators and links

- Section II, pp. 2–3, Properties P1–P3 and Theorem 2.
- Section III, Eqs. (8)–(12), tomography.
- p. 7, Theorem 4; pp. 8–9, Choi/MPO and environment dimension.
- Claims: `C004`, `C005`, `C023`; rivals: `R001`, `R002`; criteria: `F001`,
  `F006`.

