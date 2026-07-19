# Pilot Batch 01 — formal core of constrained futures

- Date: 2026-07-19
- Protocol: 0.2
- Scope: constructor theory, quantum process memory, computational mechanics,
  macrostates/path ensembles, and causal semantics
- Evidence base: 18 peer-reviewed primary/formal sources, plus one current
  author-review background source; 31 source-claim relations
- Status: bounded pilot, not a systematic review and not a conclusion about all
  seven literature programs

## Outcome first

The pilot supports a narrow and useful claim: several mature formalisms describe
how distinctions in a system's history or present effective state correspond to
different future laws. It does **not** support the stronger claim that these
formalisms have already discovered one partition-independent physical quantity
called inherited constraint.

The strongest candidate common object is relational and indexed:

`E_tau(m; Pi, A, B) = {P^pi_A(F[0:tau] | m, B) : pi in Pi}`

where:

- `m` is a proposed present record or predictive state;
- `Pi` is the admissible intervention or control family;
- `A` is the observable algebra or measurement set;
- `B` declares the system boundary, resolution, and resource assumptions;
- `E_tau` is the family of operational future laws at horizon `tau`.

This formulation is intentionally more modest than an ontology. It makes the
dependencies that existing theories require impossible to hide.

## What the three strongest neighbors actually contribute

### Constructor theory: hard transformation possibility

Constructor theory gives the cleanest native language for statements of the
form "this transformation is possible" or "its inverse is impossible." It also
ties information variables to physically possible copying, permutation, and
distinguishability tasks. The photonic homogenizer work demonstrates that a
constructor-based asymmetry can be compatible with time-reversal-symmetric
quantum laws in a specified model.

The probability paper sharpens a boundary that matters for ICP: under strong
conditions, constructor-theoretic weights can guide decisions *as if* they were
probabilities, but this is not a derivation of an objective stochastic law or of
the Born rule. An independent categorical formalization also shows that
possible tasks can be represented inside a supplied reference process theory.
That creates a serious redundancy test for ICP as well as for constructor
theory: the new language needs restrictive content beyond redescription.

Its ICP value is real but bounded. A possible task is not yet a finite-time
reachable-set support, a probability distribution over paths, a predictive
equivalence class, or a history-formed record. Those bridges must be derived,
not asserted through the shared word "possibility."

### Quantum process tensors: operational history under intervention

Process tensors are the closest match to the intervention-indexed part of the
ICP schema. For a fixed system boundary and time grid, they map a sequence of
physical control operations to a future state and all resulting measurement
probabilities. Causal breaks provide an operational test of whether information
from the earlier history still influences the future after the reduced system
state is overwritten.

The same literature supplies the decisive limitation. Memory is relative to a
system-environment partition, temporal resolution, and instrument set. A larger
state can absorb the apparent history dependence. Quantum Markov order is
generally instrument-specific, and an observed multi-time process rarely
identifies a unique microscopic carrier.

The 2025 superconducting-qubit experiment is an important empirical anchor: it
reconstructs a full three-time process and detects correlated, partly quantum
noise beyond a Markov product description. It does not establish an invariant
measure of inherited organization.

### Computational mechanics: minimal predictive memory

Computational mechanics supplies the strongest exact `H -> M -> P(F | M)`
construction. Causal states are equivalence classes of histories with identical
future conditional distributions; under the stated assumptions they are
minimal optimal predictors. Epsilon-transducers extend this idea to future
output laws under every allowed future input sequence.

This is close prior art for ICP. It means that "histories are equivalent when
they have the same futures" is not by itself new. The possible ICP contribution
must be stronger: the state must be physically embodied, formed or maintained
through a history, causally testable through intervention, and robust to
reasonable changes of representation. Predictive sufficiency alone establishes
none of those properties.

## Four distinctions the paper must enforce

| Question | Formal object | What it establishes | What it does not establish |
|---|---|---|---|
| Can a repeatable transformation be performed? | constructor-theoretic task | hard modal possibility under declared resources | finite-time path probability or inherited history |
| How do sequential controls affect later observations? | process tensor | complete operational intervention-response law in a declared span | unique carrier, partition invariance, or cross-world coupling |
| Which histories predict the same future? | causal state or epsilon-transducer state | minimal predictive equivalence | physical embodiment or intervention causality |
| What path law follows from selected constraints? | Maximum Caliber or related path ensemble | an inferential distribution over trajectories | that the constraints are physically carried by the system |

These objects may be connected in particular models, but they are not
interchangeable.

## A provisional operational criterion for inherited constraint

Call `M` an **operational inherited-constraint state** only relative to a tuple
`(Pi, A, B, tau)` and only when all five conditions are met:

1. **Formation:** controlled differences in prior history reliably produce
   distinguishable present realizations of `M`.
2. **Sufficiency:** within the declared boundary, systems with the same `M`
   have the same future-law family `E_tau` to stated tolerance.
3. **Discrimination:** at least two realizations `m1` and `m2` differ under some
   allowed intervention:

   `exists pi in Pi : D(P^pi_A(F | m1), P^pi_A(F | m2)) > delta`.

4. **Carrier test:** erase, replace, or perturb the proposed physical carrier
   while controlling material, energetic, geometric, and boundary confounds;
   the future laws change as predicted.
5. **Robustness:** the result survives justified state enlargement and
   equivalent representations, or its dependence on scale and partition is
   made part of the claim.

This is a proposed synthesis criterion, not a result already established by the
literature. It turns "information constrains the future" into an experimental
program and exposes the cases where ICP would be redundant.

## Novelty and redundancy boundary

Pilot Batch 01 rules out four weak novelty claims:

- histories compressed by their predictive futures already have a mature
  formal theory;
- input-indexed future distributions already exist in classical and quantum
  process formalisms;
- non-Markovianity alone does not prove irreducible historical inheritance;
- a constraint used to infer a distribution is not automatically a physical
  constraint carried by the system.

ICP remains scientifically interesting if it can add at least one of the
following:

- an embodiment criterion connecting a minimal operational state to specific
  physical degrees of freedom;
- an invariant or controlled equivalence class robust across justified
  partitions and coarse-grainings;
- a theorem connecting constructor-level impossibility to finite-time process
  support under explicit resources;
- a measurable compression or prediction gain beyond the best complete-state
  dynamical and process model;
- a successful carrier intervention that changes future laws while standard
  confounds are held fixed.

## Provisional graded conclusions

### Established field results

- Possible and impossible tasks provide a physical modal vocabulary for
  transformations.
- Process tensors encode complete multi-time operational statistics relative
  to declared interventions.
- Causal breaks test operational quantum memory.
- Causal states and epsilon-transducers are minimal predictive descriptions
  under their assumptions.
- Projection and state augmentation can create or remove apparent memory in a
  reduced description.
- Prediction, intervention, and counterfactual comparison are not synonymous.

### Supported synthesis inferences

- The recurring formal motif is a **family of future laws indexed by operational
  choices and boundaries**, not a universal scalar information measure.
- A physically meaningful ICP state must be stronger than predictive
  information: it needs a carrier, an intervention test, and declared
  representation dependence.

### Qualified or rejected inferences

- "Constructor-possible" cannot be substituted for nonzero path probability.
- Quantum non-Markovianity cannot by itself establish a fundamental inherited
  constraint.
- A causal state cannot be assumed to be a localized physical object.
- Maximum-Caliber constraints cannot be cited as evidence of material
  constraint without an independent mechanism.
- No source in this pilot identifies unit-level cross-world counterfactuals from
  predictive distributions alone.

## How this starts the larger ICP grounding

This batch is deliberately the formal spine, not a review selected around the
Dirac manuscript. It supplies comparison rules that the remaining pillars must
pass. The next evidence batches should apply the same operational criterion to:

1. decoherence, environmental records, and quantum Darwinism;
2. relational quantum states and observable algebras;
3. biological organization, heredity, repair, and constraint closure;
4. a Zipf mechanism-discrimination study using sequence shuffling and competing
   generative models;
5. the black-hole information frontier, separating global encoding,
   reconstruction, operational access, and computational recoverability.

The most useful immediate next bite is Zipf: it can demonstrate, with data, why
a striking marginal pattern is not evidence for inherited constraint unless it
predicts sequential and interventional differences beyond the marginal.
