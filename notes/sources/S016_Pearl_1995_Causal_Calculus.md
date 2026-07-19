# S016 — Pearl (1995), A Causal Calculus for Statistical Research

## Bibliographic record

- Citation key: `Pearl1995CausalCalculus`
- Stable URL: <https://proceedings.mlr.press/r0/pearl95a.html>
- Status: peer-reviewed proceedings article
- Stratum: cross-cutting causal semantics

## Why included

Establishes the semantic guardrail needed for the user's interest in
counterfactual future states.

## Native result and formalism

The paper distinguishes ordinary conditioning from the distribution generated
by externally setting a variable, and supplies graphical rules for combining
observation and intervention under explicit structural assumptions.

## Common-schema mapping

- `H`: observed covariate/history values.
- `M`: causal variables and structural relations, not a memory state by itself.
- `Pi`: interventions licensed by the structural model.
- Future object: population interventional outcome distribution; unit-level
  counterfactuals require still stronger structural coupling.
- Claim type: causal-interventional and identification-theoretic.

## Assumptions, limitations, and rival reading

A valid graph or structural-equation model is required. Two predictive or even
interventional marginals do not identify a joint distribution over what the
same unit would have done under mutually exclusive actions.

## Locators and links

- Abstract and pp. 430–431, conditioning versus setting; remainder for
  structural semantics and the three inference rules.
- Claims: `C022`, `C023`; rivals: `R005`; criteria: `F002`, `F004`.
