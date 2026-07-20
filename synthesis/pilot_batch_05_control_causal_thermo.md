# Bounded closure: control, causal information, and information thermodynamics

- Search cutoff: 2026-07-20
- Review role: adversarial closure for the Information-Constraint Principle (ICP)
- Scope: classical reachability and viability; empowerment and causal future-option
  objectives; interventional and semantic information; feedback information
  thermodynamics
- Evidence base: 12 peer-reviewed primary works and one current experimental
  preprint
- Status: targeted critical synthesis, not a systematic review

## Outcome first

This literature gives IOTA/ICP **real but sharply bounded scientific legs**.
It establishes four ingredients that the program needs:

1. accessible futures can be defined rigorously relative to dynamics, controls,
   disturbances, horizons, and target or admissible sets;
2. controllable future distinctions can be quantified information-theoretically;
3. causal relevance can be tested by interventions rather than inferred from
   correlation alone; and
4. physically retained measurement or environmental memory can alter later
   control performance and extractable work.

The same literature removes most of the easy novelty claims. Reachable sets,
viability kernels, empowerment, causal path entropy, causal information flow,
viability-based semantic information, and information-to-work conversion all
predate ICP. Therefore neither “the present constrains the future,” “information
changes future options,” nor “information can have physical consequences” is a
distinctive ICP result.

The defensible candidate contribution is narrower:

> **Interaction-formed constraint transport:** a physically realized causal
> role, created by prior interaction, remains operationally equivalent across
> replacement of its original local witness, and intervention on the successor
> witness changes a preregistered future-law family.

That target matches the bounded IOTA result better than generic “future
possibility” language. IOTA GC-001 reports restoration of a tracked connectivity
relation through a causally necessary successor bridge disjoint from the
predecessor bridge. Control theory can calculate the resulting reachable sets,
but the empirical object of interest is the *formation and transport of the
role across carrier replacement*. None of the sources below establishes that as
a universal physical principle.

The honest verdict from this closure is therefore:

- **Viable research program:** yes.
- **Useful cross-domain operational synthesis:** yes, if the comparison
  variables and intervention families are explicit.
- **Already established new physical principle:** no.
- **Support here for information as the fundamental substrate or for emergence
  of mass and energy:** no. These remain IOTA postulates/research targets, not
  consequences of control or information thermodynamics.

## The nearest established formalisms

| Program | Native object | What is established | Direct overlap with ICP | What it does not provide | Redundancy pressure |
|---|---|---|---|---|---|
| Hamilton–Jacobi reachability | finite-horizon reachable or backward-reachable set under specified controls and disturbances | nonlinear controlled future sets can be represented by a value function/HJI equation | almost exactly the hard-support part of `R^pi` | no requirement that history formed a record; no carrier or transport claim | very high |
| Viability theory | viability kernel inside a declared admissible set | states from which at least one admissible evolution remains within constraints can be characterized and approximated | future survival/continued accessibility under a policy | admissible set and dynamics are supplied; no account of why the constraint exists or persists | very high |
| Empowerment | channel capacity from present action sequences or feedback policies to future sensed states | controllable future distinctions can be assigned a scalar in bits | “future options under interventions” | agent/sensor/action partition and channel are supplied; equal capacities can hide different futures; no record-formation criterion | very high for scalar optionality claims |
| Causal entropic forcing | gradient of finite-horizon path entropy | a chosen drive toward larger future path entropy produces adaptive-looking behavior in simple simulations | exploration of counterfactual future paths | a proposed objective/force, not evidence that physical systems universally maximize options; no carrier | high if ICP asserts maximization; low if it does not |
| Causal information flow | divergence among post-intervention outcome laws | causal influence can be quantified when the causal model/interventions are known | intervention-indexed future-law differences | generally cannot discover the causal graph from passive data; not a material carrier theory | high for generic “causal information” |
| Viability-based semantic information | correlations whose scrambling reduces a system's later viability | a formal counterfactual test separates viability-relevant from irrelevant correlation | closest prior formalism to “information that makes a causal difference” | depends on system/environment cut, horizon, viability function, initial ensemble, and intervention choice; formal/toy-model evidence | extremely high |
| Feedback information thermodynamics | generalized work/free-energy inequalities with information terms | measurement-conditioned feedback can convert acquired information into work within ordinary thermodynamics | a stored distinction selects later physical transformations | assumes Hamiltonians, baths, energy, apparatus, and protocols; does not derive energy or ontology from information | high for “information is physical,” low for carrier transport |
| Non-Markovian information engine | hidden environmental degrees retain history that repeated measurements can exploit | current preprint reports history-dependent relaxation and enhanced work extraction from a viscoelastic bath | direct physical example of retained history affecting later transformation capacity | pre-peer-review; enlarged state is Markovian and hidden modes carry ordinary excess free energy | direct support plus a decisive state-augmentation null |

## 1. Classical reachability and viability

### 1.1 Reachability already is a theory of counterfactual futures

Mitchell, Bayen, and Tomlin prove that a continuous backward-reachable set for
a nonlinear differential game is the zero sublevel set of the viscosity
solution of a time-dependent Hamilton–Jacobi–Isaacs equation. Their definition
explicitly quantifies over opposing input signals and a finite horizon; the
method treats nonlinear dynamics and uncertain time-varying disturbances. See
Theorem 2 and Eqs. (3)–(6) in [Mitchell, Bayen & Tomlin (2005),
DOI:10.1109/TAC.2005.851439](https://doi.org/10.1109/TAC.2005.851439).

- Evidence status: peer-reviewed formal theorem plus numerical implementation
  and an analytically checkable collision-avoidance example.
- ICP relationship: direct formal neighbor for hard reachability.
- Strongest limitation: the dynamics, state boundary, target, controls,
  disturbance model, information pattern, and horizon are inputs. The reachable
  set does not explain the formation or physical persistence of any constraint.
  The paper also notes exponential grid cost with state dimension.

**Adversarial conclusion:** If ICP only maps a fully specified present state and
intervention to its reachable set, it is standard reachability theory under new
vocabulary.

### 1.2 Viability already formalizes “keeping possibilities alive”

Saint-Pierre defines discrete viability kernels and proves convergent
approximation of a continuous viability kernel for differential inclusions by
recursive discrete and finite kernels. The kernel is the largest domain from
which an admissible evolution can remain within the declared constraint set.
See the abstract and main approximation results in [Saint-Pierre (1994),
DOI:10.1007/BF01204182](https://doi.org/10.1007/BF01204182).

- Evidence status: peer-reviewed formal analysis.
- ICP relationship: direct neighbor for persistence within a future-admissible
  region.
- Strongest limitation: the acceptable region, differential inclusion, and
  admissible actions are supplied. A viability kernel is not a history-created
  record, and it need not be physically embodied in a localized witness.

**Adversarial conclusion:** “Preserving viable futures” is not new. ICP must ask
how a constraint role is created, materially carried, transferred, and
causally tested—not merely whether a viable policy exists.

## 2. Empowerment and future-option objectives

### 2.1 Empowerment is the closest scalar competitor

Klyubin, Polani, and Nehaniv define `n`-step empowerment as the channel capacity
from an action sequence to a later sensory state, maximizing mutual information
over the action distribution. It is explicitly interpreted as potential
perceivable control—what the agent *could* do, not what it actually does. See
Sec. 2.2, especially Eq. (3), and Sec. 4 in [Klyubin, Polani & Nehaniv (2005),
DOI:10.1109/CEC.2005.1554676](https://doi.org/10.1109/CEC.2005.1554676).

- Evidence status: peer-reviewed IEEE conference paper; formal definition and
  simple evolutionary simulations.
- ICP relationship: direct competitor to any scalar “number/diversity of
  counterfactual futures” measure.
- Strongest limitation: empowerment is relative to a selected action channel,
  sensor, horizon, and state representation. Channel capacity collapses outcome
  identity and structure into one scalar, and no historical carrier or
  carrier-replacement condition is required.

Tiomkin, Salge, and Polani replace fixed open-loop action scripts with feedback-
conditioned probing policies. Their process empowerment is designed to capture
controllability through noise and traps that open-loop empowerment misses; the
paper's gridworld studies show the difference on a “windy bridge.” See Secs.
2–5, especially the process-empowerment definition in Eq. (9), Fig. 4, and the
discussion in [Tiomkin, Salge &
Polani (2025), DOI:10.1088/2632-072X/adf2ec](https://doi.org/10.1088/2632-072X/adf2ec).

- Evidence status: peer-reviewed theory, algorithms, and simulations.
- ICP relationship: an especially close match to the policy-indexed family
  `{P^pi(F|M)}` because feedback is internal to the prospective policy.
- Strongest limitation: demonstrations are supplied computational environments;
  the model presupposes the agent/world/sensor/action decomposition and does not
  identify a physical record formed by history.

### 2.2 Causal entropic forces are not evidence of a universal drive

Wissner-Gross and Freer propose a force proportional to the gradient of a
finite-horizon causal path entropy and show tool-use- and cooperation-like
behavior in simple simulations. See the model and simulation results in
[Wissner-Gross & Freer (2013), DOI:10.1103/PhysRevLett.110.168702](https://doi.org/10.1103/PhysRevLett.110.168702).

- Evidence status: peer-reviewed theoretical proposal and simulation.
- ICP relationship: contextual/competitive if ICP is framed as a tendency to
  preserve or maximize future alternatives.
- Strongest limitation: the path measure, horizon, and causal-temperature scale
  are model choices, and the simulations show behavior under the added force;
  they do not demonstrate that ordinary physical systems possess such a
  universal force.

ICP should therefore say explicitly:

> ICP does not assert that systems maximize future-state count, empowerment, or
> causal path entropy. It asks whether interaction-formed physical organization
> changes the family of futures and whether that causal role can persist across
> replacement of its original witness.

If ICP later adds a maximization principle, causal-entropic forcing and
empowerment become mandatory quantitative baselines.

## 3. Causal and semantic information

### 3.1 Intervention, not prediction, identifies causal relevance

Ay and Polani define information flow from post-intervention distributions,
using causal independence rather than observational association. They also
stress that in an experiment the causal model is generally unknown and active
intervention is the direct route to identifying effects; their measure
quantifies influence given the model rather than discovering it. See Secs. 3–7,
especially Sec. 7, in [Ay & Polani (2008),
DOI:10.1142/S0219525908001465](https://doi.org/10.1142/S0219525908001465).

- Evidence status: peer-reviewed formal framework and worked models.
- ICP relationship: direct support for indexing future laws by declared
  interventions.
- Strongest limitation: intervention distributions and the causal graph must be
  justified; a nonzero number does not locate a material carrier.

James, Barnett, and Crutchfield give counterexamples in which transfer entropy
and causation entropy overestimate flow or underestimate influence, and show
that dyadic measures can miss polyadic dependencies. See the examples and
conclusion in [James, Barnett & Crutchfield (2016),
DOI:10.1103/PhysRevLett.116.238701](https://doi.org/10.1103/PhysRevLett.116.238701).

- Evidence status: peer-reviewed formal counterexamples/critique.
- ICP relationship: direct methodological warning.
- Strongest limitation: it rules out a common inference, not causal analysis in
  general.

**Required consequence for ICP:** observational mutual information, predictive
information, transfer entropy, or a Zipf statistic cannot by itself establish
that `M` constrains `F`. ICP needs an intervention on the proposed physical
carrier or an identified causal model with independently defended assumptions.

### 3.2 Viability-based semantic information is the strongest conceptual rival

Kolchinsky and Wolpert define semantic information as syntactic correlation
between a system and environment that is causally necessary for the system's
later viability. Their counterfactual intervention scrambles selected
correlations while leaving marginal distributions controlled; stored and
observed variants use initial mutual information and dynamically acquired
transfer entropy, respectively. See Sec. 5, especially Eqs. (5.1)–(5.10), and
Secs. 6–7 in [Kolchinsky & Wolpert (2018),
DOI:10.1098/rsfs.2018.0041](https://doi.org/10.1098/rsfs.2018.0041).

- Evidence status: peer-reviewed formal/conceptual framework with toy models;
  not an empirical demonstration of a universal quantity.
- ICP relationship: closest prior art to “a distinction matters if removing it
  changes what happens later.”
- Strongest limitation: the quantity is relative to a system/environment split,
  horizon, initial ensemble, syntactic measure, viability function, and allowed
  scrambling interventions. It targets self-maintenance/viability, not arbitrary
  future-law structure, and does not require persistence across replacement of a
  physical witness.

This produces a hard novelty test:

- If an ICP analysis chooses “continued existence” as its target and correlation
  scrambling as its intervention, it should use or specialize the
  Kolchinsky–Wolpert framework rather than rename it.
- Merely replacing viability with an arbitrary future variable makes ICP
  broader but not automatically deeper; broadness without an invariant or new
  result is a loss of specificity.
- ICP's plausible distinction is the explicit **formation–transport–successor
  carrier** sequence and its reachability-role equivalence, applicable without
  an agent or viability objective.

## 4. Feedback information thermodynamics

### 4.1 Information changes thermodynamic performance inside established physics

Sagawa and Ueda derive a generalized Jarzynski equality for measurement-based
feedback. Mutual information and feedback efficacy enter the fluctuation
relation, yielding bounds that differ from uninformed control. See the main
work bound and generalized equality, Eqs. (3)–(4), and the information-ratchet
example in [Sagawa & Ueda (2010),
DOI:10.1103/PhysRevLett.104.090602](https://doi.org/10.1103/PhysRevLett.104.090602).

Toyabe and colleagues experimentally implement real-time feedback on a Brownian
particle in a switchable potential. Position information selects the feedback;
the particle gains free energy beyond the directly applied work and the data
test the generalized Jarzynski equality. See Figs. 2–4 and Methods in [Toyabe et
al. (2010), DOI:10.1038/nphys1821](https://doi.org/10.1038/nphys1821).

- Evidence status: peer-reviewed formal theory and a direct colloidal
  experiment.
- ICP relationship: strong evidence that a recorded distinction used to choose
  a protocol changes a later physical transformation and work balance.
- Strongest limitation: the controller, measurement, energy landscape, heat
  bath, and feedback rule are supplied. This demonstrates information-to-work
  conversion within a theory that already contains energy; it does not show
  that energy emerges from information or that mutual information is an
  ontological substrate.

### 4.2 Autonomous memory closes an important bookkeeping loophole

Mandal and Jarzynski exactly solve a minimal autonomous Maxwell demon that
interacts sequentially with a tape of bits. Depending on parameters, the device
extracts work while writing information or consumes work while erasing it. See
the model, phase diagram, and steady-state analysis in [Mandal & Jarzynski
(2012), DOI:10.1073/pnas.1204263109](https://doi.org/10.1073/pnas.1204263109).

- Evidence status: peer-reviewed exact stochastic model.
- ICP relationship: physically explicit memory carrier and dynamics, more
  relevant than an abstract external observer.
- Strongest limitation: it is a designed model with a supplied tape, energy
  levels, thermal reservoir, and transition rates. It does not create a
  carrier-independent constraint role.

Hartle and colleagues treat noisy measurements, finite memory, and a limited
repertoire of work-extraction protocols. They construct protocol repertoires
that minimize expected thermodynamic loss and show that feedback benefits need
not be summarized by information gain alone. See the model and optimization
results in [Hartle et al. (2026),
DOI:10.1103/h2b9-gkd8](https://doi.org/10.1103/h2b9-gkd8).

- Evidence status: peer-reviewed theoretical result, *Physical Review
  Research* 8, 013281 (2026).
- ICP relationship: direct support for carrying resources and the admissible
  protocol repertoire inside every future-law claim.
- Strongest limitation: a task-specific harvesting framework; no emergent
  carrier or universal physical law.

### 4.3 A current experiment makes environmental memory unusually concrete

Muruga and colleagues report a 2026 experiment on an optically trapped colloid
in a viscoelastic micellar bath. Time-delayed double measurements distinguish
relaxation curves not fixed by the visible instantaneous state; feedback in a
double-well protocol extracts work exceeding the visible particle's initial
potential energy, attributed to excess free energy in hidden environmental
degrees of freedom. The paper explicitly notes that the enlarged state
`Z={X,Y}` is Markovian and derives an extra conditional-information term for
the hidden degrees. See Eqs. (1)–(13), Figs. 2–4, and Methods in [Muruga et al.
(2026), arXiv:2603.06160](https://arxiv.org/abs/2603.06160); processed data and
code are registered at [Zenodo DOI:10.5281/zenodo.18715334](https://doi.org/10.5281/zenodo.18715334).

- Evidence status: primary experiment with public processed data/code, but a
  preprint as of the search cutoff; not yet peer reviewed or independently
  replicated.
- ICP relationship: the most direct source in this batch for history retained
  outside the visible degree of freedom changing later energetic capability.
- Strongest limitation: it simultaneously vindicates the state-augmentation
  null. Memory is ordinary correlation/excess free energy in hidden bath modes
  under a reduced description, not evidence of information independent of all
  physical realization.

This source supports a precise phrase for the synthesis:

> Information can persist separately from the *original or currently observed
> bearer* while remaining physically realized in other degrees of freedom.

It does not support “information persists without a physical realization.”

## 5. Formal ICP comparison and novelty gate

Let the standard controlled model have complete state `z_t`, transition law
`T`, admissible policy family `Pi`, observable algebra `A`, boundary/resource
declaration `B`, and horizon `tau`. Define the operational future-law family

`E_tau(z; Pi,A,B) = {P_A^pi(F[0:tau] | z,B) : pi in Pi}`.

Control and process-empowerment theory already supply versions of this object.
The null model is:

`M_t = g(z_t)` and every claimed ICP effect is derivable from
`(T,z_t,Pi,A,B)`.

Under that null, “information constrains the future” is true but redescriptive.

The carrier-transport target can instead be written as a role equivalence:

`m ~_(Pi,A,B,tau) m'`

iff the two physical realizations induce the same preregistered operational
future-law family to the declared tolerance. A strict transport event requires:

1. interaction history creates a role-bearing realization `m` that was absent
   initially;
2. the original local witness ceases to realize the role;
3. a disjoint or lineage-defined successor `m'` satisfies the role equivalence;
4. a matched intervention on `m'`, but not a sham or equal-cost role-preserving
   intervention, changes the declared future law; and
5. the result survives predeclared changes of representation, boundary, and
   probe family that should count as physically equivalent.

IOTA GC-001 supplies a bounded candidate for items 2–4 in a connectivity task;
the larger IOTA program must establish formation from an initially absent role
case by case. It does not yet establish item 5, iterated/indefinite transport,
or a general law. This is nevertheless a more defensible scientific starting
point than a new future-set scalar.

### Mandatory redundancy and novelty tests

1. **Complete-state reachability test.** Compute the same endpoints with the
   ordinary transition kernel on the enlarged state `(X,G,environment)`. If ICP
   supplies no new invariant, compression, prohibition, or held-out prediction,
   classify it as an interpretation/research heuristic.
2. **Empowerment baseline.** Compare any ICP scalar with reach-set cardinality,
   reach-volume, open-loop empowerment, and process empowerment on identical
   states, actions, observations, horizons, and resources. Equal scalar values
   with different future laws must remain distinguishable in ICP.
3. **Semantic-information baseline.** On viability tasks, compute
   Kolchinsky–Wolpert semantic information under the same partition and
   intervention. Report whether ICP is a specialization, extension, or gives a
   genuinely different prediction.
4. **Carrier necessity and specificity.** Randomize, delete, swap, or replace
   the proposed successor witness with matched material, geometry, state-count,
   and intervention-cost controls. Include a role-preserving intervention and
   an equal-cost role-breaking intervention.
5. **Transport rather than survival.** Require loss of the original witness and
   restoration through a disjoint or independently traced successor. Mere
   longevity or hidden-state memory does not pass.
6. **Boundary/representation audit.** Repeat over justified system cuts,
   coarse-grainings, temporal resolutions, and observable sets. State which
   changes are physical and which are coordinate/redescription changes.
7. **Closed thermodynamic accounting.** Where work or heat is claimed, include
   measurement, memory, reset, controller, and protocol costs. An autonomous
   implementation is stronger than a cost-free external controller.
8. **Ontology ladder gate.** Feedback conversion cannot support “energy emerges
   from information” because it assumes energy. Progress on the IOTA emergence
   ladder requires deriving stable quasiparticle roles, composition and
   interaction, effective generators/conservation, and only then mass- or
   energy-like observables from the informational construction.

## 6. Proposed claim–evidence rows

These are provisional merge rows; assign project `S` and `C` identifiers only
after deduplication against the shared registries.

| Row | Claim level | Proposed claim | Source and exact locator | Evidence type | Prediction/intervention status | Direction / directness | Strongest alternative or limit |
|---|---|---|---|---|---|---|---|
| CC01 | `field_result` | A finite-horizon backward-reachable set for a nonlinear differential game is characterized as the zero sublevel set of a time-dependent HJI viscosity solution. | Mitchell et al. 2005, Sec. II.A–B, Eqs. (3)–(6), Theorem 2 | formal theorem + numerical validation | interventional/control | qualifies, direct | fully specified ordinary dynamics and inputs already generate the future set |
| CC02 | `field_result` | Viability kernels can be approximated by recursive discrete/finite kernels under stated regularity conditions. | Saint-Pierre 1994, abstract and main convergence results | formal theorem | control/existential-policy | qualifies, direct | constraint set and dynamics are externally supplied; no record formation |
| CC03 | `field_result` | `n`-step empowerment is the channel capacity from present action sequences to later sensory states and measures potential perceivable control. | Klyubin et al. 2005, Sec. 2.2 Eq. (3), Sec. 4 | formal definition + simulations | interventional/open-loop | challenges novelty, direct | agent partition, channel, representation, and horizon determine the scalar |
| CC04 | `field_result` | Process empowerment incorporates feedback-conditioned probing and can identify controllable futures that open-loop scripts miss under noise. | Tiomkin et al. 2025, Secs. 2–5, Eq. (9), Fig. 4 | theory + algorithms + simulations | interventional/feedback | challenges novelty, direct | supplied gridworlds; no history-formed physical carrier |
| CC05 | `field_result` | Causal information flow quantifies differences among post-intervention laws but presupposes a defended causal model or experimental intervention. | Ay & Polani 2008, Secs. 3–7, especially Sec. 7 | formal framework | interventional | supports, direct | passive observations generally do not identify the required causal structure |
| CC06 | `field_result` | Transfer entropy and causation entropy can both overestimate flow and underestimate influence, and dyadic analysis can miss polyadic dependence. | James et al. 2016, examples and conclusion | formal counterexamples | predictive, not sufficient for causal | challenges, direct | rejects a proxy, not all causal-information measures |
| CC07 | `field_result` | Semantic information can be defined as system–environment correlation whose counterfactual scrambling reduces later system viability. | Kolchinsky & Wolpert 2018, Sec. 5, Eqs. (5.1)–(5.10), Secs. 6–7 | formal/conceptual + toy models | counterfactual in model | challenges novelty, direct | depends on viability, partition, horizon, ensemble, and scrambling family; no carrier replacement |
| CC08 | `field_result` | Generalized feedback fluctuation relations include measurement information and feedback efficacy, altering work bounds. | Sagawa & Ueda 2010, Eqs. (3)–(4) and information-ratchet example | formal statistical physics | feedback-interventional | supports, partial | assumes energy, bath, measurement, and protocol; no ontological emergence |
| CC09 | `field_result` | Real-time position-conditioned feedback on a Brownian particle converts acquired information into free energy and tests the generalized Jarzynski equality. | Toyabe et al. 2010, Figs. 2–4 and Methods | experiment | feedback-interventional | supports, partial | external apparatus/controller and ordinary energetics provide the mechanism |
| CC10 | `field_result` | Time-delayed measurements of a colloid in a viscoelastic bath reveal hidden environmental memory and enable work extraction beyond the visible-state energy bound in a double-well protocol. | Muruga et al. 2026, Eqs. (1)–(13), Figs. 2–4, Methods | experiment, preprint | feedback-interventional | supports, direct but immature | enlarged state is Markovian; hidden modes carry ordinary excess free energy; not peer reviewed |

## 7. How this should change the synthesis paper

The main text should not introduce control and information thermodynamics as an
eighth confirming pillar. They are the **formal baseline and adversarial null**
against which every pillar is judged.

Recommended framing:

1. Start from the IOTA postulate as project ontology, clearly labeled as a
   postulate rather than literature-derived fact.
2. Define ICP operationally through the indexed future-law family, but state
   immediately that control/process theories already provide that mathematical
   object.
3. Make the proposed addition the formation and transport of a physically
   embodied constraint role across carrier succession.
4. Present GC-001 as bounded project evidence for one relational role, with its
   three positives, finite lifetimes, non-universality, and supplied lattice law
   intact.
5. Use semantic information as the closest prior formal competitor and the 2026
   environmental-memory experiment as the closest current physical analogy.
6. State that information thermodynamics establishes operational conversion and
   accounting relationships, not information's ontological priority.
7. Reserve the IOTA emergence ladder—constraint transport to coherence,
   quasiparticles, fields/conservation, then mass and energy—as the prospective
   research program.

### Suggested graded conclusion for this flank

> Established science already treats future accessibility as relative to
> dynamics, interventions, resources, and system boundaries; it already
> quantifies controllable future distinctions and demonstrates that retained
> correlations can change feedback performance and work extraction. IOTA's
> bounded contribution is not the discovery that present state constrains the
> future. It is a controlled example in which an interaction-generated
> relational role is restored through a disjoint, causally necessary successor
> realization. That result makes carrier succession a credible target for a
> broader Information-Constraint Principle, but neither it nor the surrounding
> literature yet establishes an invariant new law, information as the unique
> physical substrate, or the emergence of mass and energy. ICP therefore has
> real legs as a falsifiable research program and synthesis framework; its
> status as a distinct physical principle depends on passing the stated
> reachability, empowerment, semantic-information, carrier, and ontology gates.

## Core primary-source register

1. P. Saint-Pierre, “Approximation of the viability kernel,” *Applied
   Mathematics & Optimization* 29, 187–209 (1994),
   [DOI:10.1007/BF01204182](https://doi.org/10.1007/BF01204182).
2. I. M. Mitchell, A. M. Bayen, and C. J. Tomlin, “A time-dependent
   Hamilton–Jacobi formulation of reachable sets for continuous dynamic
   games,” *IEEE Transactions on Automatic Control* 50, 947–957 (2005),
   [DOI:10.1109/TAC.2005.851439](https://doi.org/10.1109/TAC.2005.851439).
3. A. S. Klyubin, D. Polani, and C. L. Nehaniv, “Empowerment: A universal
   agent-centric measure of control,” *IEEE Congress on Evolutionary
   Computation*, 128–135 (2005),
   [DOI:10.1109/CEC.2005.1554676](https://doi.org/10.1109/CEC.2005.1554676).
4. S. Tiomkin, C. Salge, and D. Polani, “Process empowerment for robust
   intrinsic motivation,” *Journal of Physics: Complexity* 6, 035011 (2025),
   [DOI:10.1088/2632-072X/adf2ec](https://doi.org/10.1088/2632-072X/adf2ec).
5. A. D. Wissner-Gross and C. E. Freer, “Causal entropic forces,” *Physical
   Review Letters* 110, 168702 (2013),
   [DOI:10.1103/PhysRevLett.110.168702](https://doi.org/10.1103/PhysRevLett.110.168702).
6. N. Ay and D. Polani, “Information flows in causal networks,” *Advances in
   Complex Systems* 11, 17–41 (2008),
   [DOI:10.1142/S0219525908001465](https://doi.org/10.1142/S0219525908001465).
7. R. G. James, N. Barnett, and J. P. Crutchfield, “Information flows? A
   critique of transfer entropies,” *Physical Review Letters* 116, 238701
   (2016), [DOI:10.1103/PhysRevLett.116.238701](https://doi.org/10.1103/PhysRevLett.116.238701).
8. A. Kolchinsky and D. H. Wolpert, “Semantic information, autonomous agency
   and non-equilibrium statistical physics,” *Interface Focus* 8, 20180041
   (2018), [DOI:10.1098/rsfs.2018.0041](https://doi.org/10.1098/rsfs.2018.0041).
9. T. Sagawa and M. Ueda, “Generalized Jarzynski equality under nonequilibrium
   feedback control,” *Physical Review Letters* 104, 090602 (2010),
   [DOI:10.1103/PhysRevLett.104.090602](https://doi.org/10.1103/PhysRevLett.104.090602).
10. S. Toyabe, T. Sagawa, M. Ueda, E. Muneyuki, and M. Sano, “Experimental
    demonstration of information-to-energy conversion and validation of the
    generalized Jarzynski equality,” *Nature Physics* 6, 988–992 (2010),
    [DOI:10.1038/nphys1821](https://doi.org/10.1038/nphys1821).
11. D. Mandal and C. Jarzynski, “Work and information processing in a solvable
    model of Maxwell's demon,” *PNAS* 109, 11641–11645 (2012),
    [DOI:10.1073/pnas.1204263109](https://doi.org/10.1073/pnas.1204263109).
12. H. Hartle, D. H. Wolpert, A. Stier, C. P. Kempes, and G. Manzano, “Work
    extraction with feedback control using limited resources,” *Physical Review
    Research* 8, 013281 (2026),
    [DOI:10.1103/h2b9-gkd8](https://doi.org/10.1103/h2b9-gkd8).
13. L. Muruga, F. Ginot, S. A. M. Loos, and C. Bechinger, “Extracting work
    from hidden degrees of freedom” (2026 experimental preprint),
    [arXiv:2603.06160](https://arxiv.org/abs/2603.06160).

## Stopping decision

This flank is at conceptual saturation for the first synthesis paper. Later
work may deepen stochastic reachability, controllability Gramians, causal
strength decompositions, or autonomous information engines, but further broad
searching is unlikely to change the present verdict. The remaining work is to
apply the novelty tests to IOTA/PSA and integrate this baseline with the quantum,
biological, entropy, Zipf, and black-hole closures.
