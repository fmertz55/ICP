# S011 — Bialek, Nemenman, and Tishby (2001), Predictive Information

## Bibliographic record

- Citation key: `BialekEtAl2001Predictability`
- DOI: <https://doi.org/10.1162/089976601753195969>
- Status: peer-reviewed theoretical article
- Stratum: statistics of prediction

## Why included

Defines a rigorous information quantity for how much a past observation window
tells us about a future window.

## Native result and formalism

Predictive information is `I(X_past; X_future)`. In the stationary block-entropy
setting it is the subextensive component of entropy. The paper analyzes finite,
logarithmic, and fractional-power growth regimes and connections to learning.

## Common-schema mapping

- `H`: finite past observation window.
- `M`: no unique carrier; the statistic measures dependence.
- `Pi`: passive observation.
- Future object: finite or asymptotic future observation window.
- Claim type: predictive association.

## Assumptions, limitations, and rival reading

Stationarity underlies the principal block-entropy identities, and asymptotics
depend on model regularity. Mutual information neither identifies causal
influence nor distinguishes hard inaccessibility from probability weighting.

## Locators and links

- Section 3, Eqs. (5)–(10); Markov specialization and state-entropy bound,
  Eqs. (16)–(18).
- Claim: `C015`; rivals: `R005`; criteria: `F001`, `F002`.

