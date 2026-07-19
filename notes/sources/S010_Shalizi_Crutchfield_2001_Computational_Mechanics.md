# S010 — Shalizi and Crutchfield (2001), Computational Mechanics

## Bibliographic record

- Citation key: `ShaliziCrutchfield2001ComputationalMechanics`
- DOI: <https://doi.org/10.1023/A:1010388907793>
- Status: peer-reviewed theoretical article
- Stratum: computational mechanics

## Why included

Foundational exact construction for compressing histories by the futures they
predict—the most important classical prior art for ICP's statistical view.

## Native result and formalism

Two pasts are causally equivalent when they induce the same conditional law over
the full semi-infinite future. The resulting causal states are maximally
predictive, minimal among equally predictive statistics, and unique up to
isomorphism. Statistical complexity is the entropy of the causal-state random
variable.

## Common-schema mapping

- `H`: semi-infinite observed past.
- `M`: causal state `epsilon(H)`.
- `Pi`: passive observation in the base epsilon-machine.
- Future object: full conditional observational future.
- Claim type: predictive, not Pearl-interventional.

## Assumptions, limitations, and rival reading

The main development assumes a stationary discrete-time process and discrete
alphabet, with access in principle to the exact process law. A causal state is a
minimal statistic; it is not automatically a localized or manipulable physical
carrier.

## Locators and links

- Definition 5 and Eq. (16).
- Theorem 1 and Corollary 1, Eqs. (21)–(23); Theorems 2–3 and Eqs. (26)–(27).
- Section VII.B, pp. 19–20, limitations.
- Claims: `C013`, `C014`, `C024`; rivals: `R003`, `R005`; criteria: `F002`,
  `F003`, `F004`.
