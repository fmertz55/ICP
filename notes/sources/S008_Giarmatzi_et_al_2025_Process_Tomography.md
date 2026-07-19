# S008 — Giarmatzi et al. (2025), Multi-time Process Tomography

## Bibliographic record

- Citation key: `GiarmatziEtAl2025Tomography`
- DOI: <https://doi.org/10.22331/q-2025-12-18-1952>
- Status: peer-reviewed experiment
- Stratum: quantum process memory

## Why included

Best current empirical cornerstone in this pilot for a fully reconstructed
multi-time quantum process on working superconducting hardware.

## Native result and method

Sequential informationally complete measure-and-prepare operations and
post-processing reconstruct a three-time process Choi matrix from in-house and
IBM superconducting processors. The analysis detects general temporal
correlations and temporal entanglement consistent with a quantum contribution
to correlated noise.

## Common-schema mapping

- `H`: different earlier measure-and-prepare sequences.
- `M`: operational process memory; environment and nearby qubits are candidate
  carriers.
- `Pi`: the reconstructed span of sequential operations.
- Future object: later joint operation and outcome probabilities.
- Claim type: experimental interventional-operational statistics.

## Assumptions, limitations, and rival reading

The experiment assumes stable operation and sufficiently accurate local
preparations and measurements. Tomography scales exponentially and the process
does not uniquely identify the microscopic carrier. Temporal entanglement is
not a general measure of inherited organization.

## Locators and links

- pp. 1–3, protocol and 324 experimental sequences.
- pp. 4–5, closest-Markov process Eq. (5), relative entropy Eq. (6), Table 1.
- pp. 5–6, temporal negativity; pp. 6–7, limitations.
- Claims: `C010`, `C011`; rivals: `R002`, `R005`; criteria: `F002`, `F006`.

