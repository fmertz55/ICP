# S013 — Barnett and Crutchfield (2015), Epsilon-Transducer

## Bibliographic record

- Citation key: `BarnettCrutchfield2015Transducer`
- DOI: <https://doi.org/10.1007/s10955-015-1327-5>
- Status: peer-reviewed theoretical article
- Stratum: controlled computational mechanics

## Why included

Closest classical prior art to grouping histories by an entire family of
future laws under allowed inputs.

## Native result and formalism

Joint input-output pasts are equivalent when they yield the same distribution
of future outputs for every future input sequence. Epsilon-transducer states
are minimal optimal channel predictors and unique under the stated conditions.

## Common-schema mapping

- `H`: joint input-output past.
- `M`: epsilon-transducer state.
- `Pi`: future input sequences admitted by the channel.
- Future object: conditional future-output process.
- Claim type: controlled prediction; intervention semantics need extra support.

## Assumptions, limitations, and rival reading

The construction assumes stationary, ergodic, discrete input-output processes
and a total, anticipation-free channel. State occupancy and complexity depend on
the input process. Conditioning on input is not necessarily `do(input)` if input
assignment is confounded or physically constrained.

## Locators and links

- Section II.1, assumptions; Section III, Definitions 1–4.
- Section VI, Eq. (51) and Definition 8; Section IX, Theorems 2–3.
- Claims: `C018`, `C019`, `C023`; rivals: `R001`, `R005`; criteria: `F001`,
  `F002`, `F004`.

