# S175 — Bianconi (2026), Thermodynamics of the gravity from entropy theory

## Bibliographic record

- Citation key: `Bianconi2026Thermodynamics`
- DOI: <https://doi.org/10.1103/26kn-thgp>
- arXiv v4: <https://arxiv.org/abs/2510.22545v4>
- Status: peer-reviewed theoretical article in *Physical Review D* 114,
  024042 (2026)

## Why this source is included

This paper develops local thermodynamic quantities for GfE and evaluates their
scaling on Friedmann backgrounds. It is the most concrete current target for
mapping a GfE quantity to an indexed ICP constraint diagnostic. Its FRW
scalings are also a mandatory null because they are obtained where GfE is
approximated by GR, not as distinctive full-GfE predictions.

## Native system and question

The system is a homogeneous and isotropic spacetime with an FRW metric. The
flattened operator modes are indexed by `k`, with degeneracies `z_k`.
Observable quantities include GfE mode variables, local geometric quantum
relative entropy, local energy, G-field components, the Hubble rate, scale
factor, pressure, and entropy. The analysis assumes perfect-fluid matter and a
low-energy, small-curvature regime.

The source asks what local entropy, energy, temperature, and pressure relations
follow from GfE and how they scale on Friedmann backgrounds.

## Native formalism and exact result

The paper uses `Theta = Gtilde gtilde^{-1}`, `Gcal = Theta^{-1}`, and
`L = -Tr_F ln Theta`. For each mode it defines

`delta s_k / delta v = ln Gcal_k`, `theta_k = Gcal_k - 1`,

with local energy contribution `Gcal_k - 1 - ln Gcal_k` and a local first-law
relation.

On Friedmann backgrounds inserted in the low-energy, small-curvature regime,
`u_k = omega_k H^2`. For modes with nonzero `omega_k`, the leading local
entropy and energy contributions scale as `H^2` and `H^4`; for non-de Sitter
solutions with `H ~ t^-1`, these become approximately `t^-2` and `t^-4`.
After summation, the leading entropy coefficient can cancel: the paper's Milne
and `w = 1` cases do not have the generic aggregate `H^2` term.

Individual entropy-mode contributions may have either sign. The reported
nonvanishing-mode scalings are GR-limit Friedmann-background asymptotics, not
predictions derived from solutions of the full nonlinear GfE equations.

## Common-schema mapping

- Physical carrier or organization: local metric/G-field mode configuration.
- Dynamics: FRW evolution and the GfE thermodynamic definitions.
- Claim type: model-conditional scaling, not a controlled intervention.
- Reachable set or future-law distribution: not defined.
- Comparison: modes, fluids, curvature regimes, and times.

No independent history variable is proposed; the scaling follows from the
declared current fields and background equations.

## Assumptions, alternatives, and ICP relationship

The geometric operators are not ordinary trace-one density matrices, and
positive-definiteness restricts the valid time and curvature domain. The
`H^2`, `H^4`, `t^-2`, and `t^-4` behavior may be a thermodynamic reexpression
of standard Friedmann scaling. No cosmological fit, unique transition, or
observational discriminator is reported.

The thermodynamic derivation is a `field_result`; mapping it to ICP is a
`synthesis_inference`. ICP would add a matched future-law contrast, carrier
manipulation, a representation-stable map, and a preregistered prediction
beyond GR and native GfE.

## Locators and linked IDs

- Sec. II.1, Eqs. (2)--(9): GfE action and relative-entropy interpretation.
- Sec. II.2, Eqs. (10)--(17): Theta, G-field, and dressed action.
- Secs. III.2--III.3, Eqs. (33)--(47): local energy, entropy, temperature,
  pressure, and first law.
- Sec. IV, Eqs. (48)--(54): Friedmann backgrounds used in the approximation.
- Sec. V, Eqs. (55)--(65): `u_k ~ H^2`, validity bounds, and local
  entropy/energy scaling.
- Sec. VI: validation and observational caveats.
- Claims: `C104`, `C105`; rival: `R033`; criterion: `F031`.

## Open questions

- How do full GfE cosmologies compare with inserted GR/Friedmann backgrounds?
- Can the theory derive a transition or observable distinct from GR and
  standard modified-gravity rivals?
- Does any local GfE quantity have a measurable carrier or intervention
  response?
