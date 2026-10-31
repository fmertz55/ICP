# Candidate quantitative forms of ICP

Date recorded: `2026-10-27`

Status: **proposed research targets; no evidence for ICP is added.** This note
records two candidate forms that could give ICP the quantitative content its
viability verdict says it still lacks. Neither has been tested. The sources
named here that are not in `library/source_index.csv` are marked
*unregistered*. They must be registered under the review protocol before any
manuscript relies on them.

## Why this note exists

The viability verdict and criterion `F001` set the bar. Once the complete
physical state, correlations, controls, resources, boundaries, and laws are
included, ICP earns distinct physical content only through a new invariant,
compression, prohibition, or prediction that survives carrier intervention,
state augmentation, and reasonable changes of representation. A framework that
describes constrained futures in a common language is useful. A principle has
to be able to come out numerically wrong.

Landauer's principle is the model to aim for. It gives a minimum cost,
`k_B T ln 2` per erased bit, and that cost has been measured. Each form below is
written so that it can fail in the same way.

---

## QF1. A cost bound on carrier succession

### Informal statement

Carrying a constraint role across a complete replacement of its carrier requires
at least a minimum dissipation or resource. That minimum is set by how much the
role constrains the future, not by how much microscopic information the old
carrier held.

### Formal sketch

Use the comparison language of `manuscript/sections/02_method_formalism.tex`:

- A history-formed carrier `m` and a matched reference carrier `m_0` have
  future-law families under a declared intervention set `Π`, observable algebra
  `𝒜`, boundary `B`, and resources `C`.
- The role's constraint is the indexed divergence
  `ℭ^π_{x,τ}(m ‖ m_0; 𝒜, B, C)` (Eq. `icp-constraint-divergence`), or its exact
  support specialization `ΔI_x` (Eq. `iota-kl-identity`).
- A **succession** is a physical process that transfers the role to a fresh
  carrier `m'`, disjoint from `m`, and then releases or erases `m`. Role
  continuation means the future-law family under `m'` matches the one under `m`
  within a declared tolerance, on the declared role algebra.

The bound comes in two layers.

**A caution first.** Transfer itself has no Landauer floor. Copying into a blank
register and then uncomputing the original from the copy can be logically
reversible (Bennett 1982, *unregistered*), so moving a role from `m` to `m'`
costs nothing in principle when a blank successor is supplied and the original
is still intact. A cost bound has to locate where irreversibility is
unavoidable.

**Layer 1: inherited, not distinctive.** Classify carriers by the role they
induce, `R = r(M)`, where `r` is the frozen role map. Correct continuation
requires the successor to distinguish role classes, so the succession must
leave mutual information `I(R; M') ≥ I_role > 0`. `I_role` is fixed by how many
role classes must be kept apart, and with what error. Irreversibility then
enters in two places:

1. **Successor preparation.** A successor drawn from thermal surroundings must
   first be reset to a standard state of at least `I_role` usable capacity.
   Landauer reset (1961, *unregistered*) costs `≥ k_B T ln 2` per bit. In other
   words, a succession consumes at least `k_B T · I_role` of nonequilibrium free
   energy, or the equivalent supply of blank capacity.
2. **Loss of the original.** In ICP's central scenario, the original carrier is
   degraded or destroyed by the environment. It can then not be reversibly
   uncomputed, and in repeated succession the role information must be
   re-acquired by measurement. The measurement-plus-memory-reset cost is then
   `≥ k_B T · I` (Sagawa and Ueda 2009, *unregistered*; generalized second law
   under feedback, S104).

So, for steady succession from thermal surroundings:

`resource consumed per succession ≥ k_B T · I_role`,

and the dissipation rate needed to keep a role alive against noise is at least
`k_B T` times the rate at which role-relevant information must be restored.

This layer is ordinary information thermodynamics. ICP must satisfy it, which
makes it a **prohibition ICP inherits**. A claimed role succession that consumes
less would refute either the claim or the accounting. On its own, it gives ICP
no distinct content.

**Layer 2: the ICP-distinctive claim, which is about scaling.** Across carriers,
the resource consumed by succession **scales with the role-level information
`I_role`, not with the carrier's microstate information `H(M)`**. Two carriers
with very different microstate entropy that induce the same role partition and
the same future-law family should show the same scaling of succession cost. A
complete-microstate copy would consume on the order of `k_B T · H(M)`.

The theoretical floor follows almost from the definitions. The empirical claim
is about *how successions that form naturally, rather than engineered copies,
actually operate*: whether their cost tracks the role or the carrier.

Closeness to the floor is not the test. Biological replication, for example,
runs many orders of magnitude above the Landauer floor. The test is which
quantity the cost scales with.

That is a **compression invariant**: the thermodynamic price of persistence is
set by the role, not by the carrier.

### What makes Layer 2 non-trivial

- If succession cost always scales with `H(M)`, ICP's role level adds nothing
  thermodynamically. Rival `R040` wins.
- If cost scales with `I_role` across carriers of different `H(M)`, the role
  partition is a physically privileged coarse-graining. It would be selected by
  dissipation, not by the analyst. This is the representation-robustness that
  `F003` demands, obtained from physics rather than imposed.

### Tests

1. **In silico, first.** Use a stochastic lattice model with explicit energy
   levels and detailed-balance rates, so dissipation is defined. Present IOTA
   laws have no temperature and cannot do this. Build carrier families that
   span at least a factor of 4 in `H(M)` at fixed `I_role`, and a factor of 4 in
   `I_role` at fixed `H(M)`. Let succession form under the model's own
   dynamics, not by an engineered copy protocol. Regress the measured resource
   per succession on `I_role` and `H(M)`.
2. **Laboratory, later.** Colloidal feedback traps and single-electron boxes
   already measure information-to-work conversion and Landauer erasure (S105;
   Bérut et al. 2012, *unregistered*). Encode one role in carriers of different
   microstate complexity and measure the succession cost.

### Failure

- **Layer 1:** any registered steady succession from thermal surroundings that
  measures below `k_B T · I_role` of consumed resource, beyond its error, is an
  accounting or claim failure.
- **Layer 2:** the fitted dependence of succession cost on `H(M)`, at fixed
  `I_role`, is not smaller than its dependence on `I_role`, at fixed `H(M)`.
  Criterion `F038`.

---

## QF2. A persistence law for roles

### Informal statement

A role persists indefinitely only if its successor graph is supercritical. Role
death is therefore an absorbing-state phase transition with measurable critical
exponents.

### Why this is not a coincidence

IOTA's own definition of indefinite persistence is "an infinite lawful path of
role-continuing successors." The existence of an infinite path in a random
successor structure is a percolation question. QF2 makes that link explicit and
quantitative.

### Formal sketch

For a tracked organization `C` with role-continuing successor set
`ℛ_C(s) = {s' : s → s' is lawful and s' continues the defining role of C}`:

- **Active unit.** A realized role-continuing successor (a role instance), not
  a lattice site.
- **Absorbing state.** `ℛ_C(s) = ∅`, the role's closed future. It is absorbing
  by definition: once no lawful role-continuing successor exists, none arises
  without a new formation event, which is a different organization.
- **Control parameter.** Any registered variable that changes successor
  redundancy, for example successor-route availability, gate opening
  probability, or medium occupation.
- **Claim QF2a.** There is a critical value `λ_c`. Below it, role survival
  `P_role(t) → 0`. Above it, `P_role(∞) > 0`. At `λ_c`,
  `P_role(t) ~ t^(−δ_role)`.
- **Claim QF2b, the class prediction.** Without extra symmetries, conservation
  laws, or permanent memory in the medium, local role succession falls in the
  directed-percolation class (Janssen–Grassberger, *unregistered*). If
  successors cannot reuse previously exhausted carriers, it falls in the
  dynamic-percolation class instead. The class follows from the role's
  succession structure, which can be determined before any run.

### The ICP-distinctive prediction

Role persistence and substrate persistence are different transitions.

The IOTA percolation protocol (`ICP-DP-PERSISTENCE-001`, in the IOTA
repository) shows analytically that under IOTA's canonical laws, any
reactivation channel plus the exact amplitude ledger makes *lattice activity*
immortal. There is no absorbing state at the substrate level. QF2 then predicts
that **roles still have a sharp death transition, at a finite `λ_c`, where the
substrate shows none.**

If role survival only ever tracks substrate survival, ICP's role level is
redundant with the substrate (rival `R041`). A role-level critical point with
measurable exponents, on a substrate that is not critical, is the first
quantitative ICP prediction that a complete-microstate description does not
state directly. Complete-microstate dynamics would still generate it, so it is a
compression claim of the kind `F001` asks for, not a new force.

### Corollary QF2c: replacement fragility near criticality

At critical percolation, large-scale connectivity is noise sensitive.
Resampling a vanishing fraction of the microscopic variables makes it nearly
independent of its prior value. QF2 therefore predicts that the probability of a
role surviving a partial carrier replacement of fixed size falls toward the
replacement-free survival baseline as `λ → λ_c⁺`. Persistence through
replacement, ICP's central phenomenon, should be robust deep in the
supercritical phase and fragile near the transition.

Context: Bezuidenhout and Grimmett (1990, *unregistered*) proved that the
critical contact process and oriented percolation die out. A 2026 claimed
resolution of the undirected dying-percolation conjecture, via Kozma and
Nitzan's 2024 reduction, is unverified and is not relied on.

### Tests

The vehicle is stage R of the IOTA percolation protocol, which is deferred until
a frozen role detector exists. It requires:

1. a role detector frozen by content hash before any run;
2. the IOTA protocol's calibrated spreading instrument (local slopes,
   bracketing, classifier) reused with roles as the active unit;
3. a matched substrate-level measurement on the same runs; and
4. for QF2c, a registered partial-replacement intervention at several distances
   from `λ_c`.

### Failure

- QF2a fails if no bracket exists in a registered range where the substrate is
  non-critical, or if role survival is indistinguishable from substrate
  survival at every evaluated point.
- QF2b fails if the measured class differs from the class predicted in advance
  from the succession structure.
- QF2c fails if replacement survival does not degrade toward criticality.

Criterion `F039`.

---

## Relation to existing criteria and rivals

| Form | Criterion | Main rival | What success would add to the verdict |
|---|---|---|---|
| QF1 Layer 1 | inherited prohibition | none; it is standard thermodynamics | consistency only |
| QF1 Layer 2 | `F038`, also `F001`, `F003` | `R040` (cost scales with carrier microstate) | a dissipation-selected role coarse-graining |
| QF2a–b | `F039`, also `F001` | `R041` (role survival is substrate survival) | the first role-level critical point with external exponents |
| QF2c | `F039`, also `F002` | `R041` | a quantitative link between criticality and replacement robustness |

## Sources to register before manuscript use

These are *unregistered* in `library/source_index.csv`:

- Landauer 1961, *IBM J. Res. Dev.* 5, 183.
- Bennett 1982, *Int. J. Theor. Phys.* 21, 905.
- Sagawa and Ueda 2009, *Phys. Rev. Lett.* 102, 250602 (minimal energy cost of
  measurement and erasure).
- Bérut et al. 2012, *Nature* 483, 187.
- Janssen 1981 and Grassberger 1982 (the DP universality conjecture).
- Hinrichsen 2000, *Adv. Phys.* 49, 815.
- Bezuidenhout and Grimmett 1990, *Ann. Probab.* 18, 1462.

These are registered: `S074` (Still et al. 2012), `S103` (Kolchinsky and
Wolpert 2018), `S104` (Sagawa and Ueda 2010), `S105` (Toyabe et al. 2010).

Cross-reference: `/Users/douglasclark/iota/specs/icp_directed_percolation_persistence/v0.1-draft/`
(`protocol.json` → `icp_mapping` and `deferred_stage`; `literature_basis.md`).
