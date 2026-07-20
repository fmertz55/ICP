# Pilot Batch 04 — Entropy as a projection of constrained possibility

- Date: 2026-07-20
- Protocol: 0.5
- Scope: thermodynamic, statistical, dynamical, path, relative, quantum,
  one-shot, algebraic, generalized, and algorithmic entropy
- Literature base: primary sources `S066` onward plus relevant sources already
  registered in Batches 01–03
- Search cutoff: 2026-07-20
- Status: cross-cutting formal stress test, not empirical confirmation of ICP

## Outcome first

Constraint does not have one entropy signature. A constraint can:

1. remove compatible states or paths;
2. reweight possibilities without removing them;
3. define which transformations are allowed;
4. select the observables or subsystem algebra whose state is described;
5. determine which distinctions matter for a task and error budget; or
6. store predictive organization while changing randomness production in an
   independent direction.

Entropy is calculated only after one of those objects has been specified. It
is therefore usually a **projection, bound, rate, or monotone of a constrained
object**, not the constraint itself.

The central result of this batch is:

> **The same entropy value does not imply the same accessible states, future
> path language, transformation preorder, observable algebra, predictive
> memory, rare-event landscape, or entropy production.**

This is the entropy version of the earlier Zipf and black-hole findings. A
Zipf marginal does not identify its generator; a Page curve does not identify
its carrier or decoder; and a scalar entropy does not identify the structure
that constrained the possibilities.

The defensible ICP thesis is consequently narrower and stronger:

> **Constraint is upstream. Entropies are task- and representation-indexed
> shadows cast by an intervention-indexed ensemble of possible futures.**

That formulation is not a new law of nature. It is a falsifiable research
discipline for deciding which entropy is relevant, what physical restriction
produces it, and what prediction remains after native theories are fully
specified.

## 1. The object that must precede entropy

Retain the project-wide future-law family

`E_tau(m; Pi,A,B) = {P^pi_A(F[0:tau] | m,B) : pi in Pi}`,

where:

- `m` is the declared present state or embodied record;
- `Pi` is the admissible intervention or operation family;
- `A` is the observable algebra or measurement family; and
- `B` contains boundary, scale, reference measure, resolution, resource, and
  error declarations.

For each policy `pi`, define the reachable path support

`Gamma_tau^pi(m;A,B) = supp P^pi_A(F[0:tau] | m,B)`.

An entropy is then a functional of some declared projection of this structure:

`S_phi = S_phi[P^pi_A, Gamma_tau^pi, O, q, epsilon, tau]`.

Here `phi` names the entropy family or operational task, `O` the allowed
operations or transformation preorder, `q` a reference state or measure, and
`epsilon` an error tolerance. Suppressing these indices invites false
equivalences.

### 1.1 Three logically separate levels

1. **Hard constraint:** changes the support, admissible path language, or
   allowed-transformation relation.
2. **Soft constraint:** changes probabilities or costs within unchanged
   support.
3. **Entropy summary:** maps the resulting object to one number, a family of
   numbers, an asymptotic rate, or an order monotone.

Only the first two are candidate physical restrictions. The third is a
measurement or representation of their consequences.

## 2. When “constraint lowers entropy” is actually valid

The slogan is a theorem only under narrow, declared conditions.

Let `C2 subset C1 subset Omega` be nested compatible-state sets measured by the
same measure `mu`. A Boltzmann-style support entropy obeys

`k log mu(C2) <= k log mu(C1)`.

Likewise, adding a feasible constraint to the *same* maximum-entropy problem
cannot increase the optimized objective, because the feasible distribution set
has become a subset.

Neither statement implies that a physical intervention called “more
constraint” must lower every entropy. The intervention may also change the
Hamiltonian, dynamics, invariant measure, observation partition, reference
state, allowed operations, boundary, or time horizon. Under those changes an
observed entropy can decrease, increase, or remain unchanged.

A correct claim must therefore state:

- what set or preorder is nested;
- what measure, algebra, and coarse-graining are held fixed;
- whether the reported entropy is an actual state property, an optimum over a
  feasible set, or an inferred ensemble; and
- which physical action implements the added constraint.

## 3. Thermodynamic entropy: a monotone of accessibility

Boltzmann's combinatorial entropy associates entropy with the multiplicity of
microstates compatible with a macrodescription (`S067`). Jaynes instead uses
Shannon entropy as an inferential objective subject to expected-value
constraints (`S068`). These are related in equilibrium statistical mechanics,
but the phrases “compatible with a macrostate” and “imposed in an inference”
do not name the same physical mechanism.

Lieb and Yngvason supply the cleaner ICP bridge. They begin with a physical
preorder of adiabatic accessibility and derive an additive, extensive entropy
that represents that order for equilibrium states under comparison and other
axioms (`S069`). In this construction the accessibility relation is logically
prior to the scalar entropy.

The boundary is as important as the result. For generic nonequilibrium states,
Lieb and Yngvason do not obtain a unique entropy with all the desired
properties. They derive lower and upper quantities, `S_-` and `S_+`, that bound
which equilibrium states can reach, or be reached from, a nonequilibrium state
(`S070`). Incomparability can therefore be real structure that a single scalar
would erase.

For ICP this means:

- an entropy may faithfully represent a sufficiently ordered accessibility
  relation;
- the existence of one scalar is not guaranteed outside that regime; and
- a proposed ICP order should be studied directly before assuming that it has
  a unique entropy representation.

## 4. Shannon entropy, entropy rate, and predictive organization

Shannon entropy answers a coding and average uncertainty question for a
declared distribution (`S066`). Temporal constraint appears only when blocks or
conditional distributions are considered. One-symbol entropy, entropy rate,
stored predictive information, and predictive-state memory are different.

Two exact examples make the point.

### 4.1 Same symbol entropy, different future structure

- IID fair coin: `H(X_t)=1`, entropy rate `h_mu=1`, excess entropy `E=0`, and
  predictive-state complexity `C_mu=0`.
- Alternating binary sequence with an initially random phase: `H(X_t)=1`,
  `h_mu=0`, `E=1`, and `C_mu=1` bit.

The marginal uncertainty is identical. The first process continually produces
randomness; the second stores one predictive bit and thereafter has a fully
constrained continuation.

### 4.2 Same support growth, different typicality

A full binary shift has topological entropy `log 2` for every Bernoulli bias
because both symbols remain possible at every step. Its measure entropy varies
as the binary entropy `H_b(p)`. Hard path possibility is unchanged while soft
weights change (`S075`–`S078`).

### 4.3 Same rates, different structures

Processes can share a scalar entropy rate or topological entropy while having
different forbidden words, causal-state graphs, synchronization behavior,
excess entropy, or intervention responses. The full future-law object cannot in
general be reconstructed from the scalar.

Computational mechanics (`S010`, `S013`) and entropy-convergence analysis
(`S081`) are therefore central prior art. They distinguish randomness produced
per step from information stored for prediction. Their causal states are
observational predictive equivalence classes unless an intervention semantics
is added.

## 5. Path entropy, rare futures, and causal restraint

Maximum Caliber maximizes Shannon entropy on a path space subject to chosen
path constraints. Transition-count constraints can yield Markov laws (`S014`).
This is a useful model-construction method, but a Lagrange multiplier does not
locate a material carrier. The selected constraint may reflect measurement,
model choice, or experimental preparation.

Large-deviation theory retains information that a mean entropy discards. A
rate function

`I_pi(a) = -lim_(tau->infinity) tau^-1 log P^pi(A_tau ~= a | m,B)`

describes the exponential cost of atypical future sectors (`S079`). Chetrite
and Touchette show how a generalized Doob transform constructs a driven process
whose typical long-time paths can represent a rare-event-conditioned ensemble
under stated spectral and convexity conditions (`S080`).

But:

> **conditioning on a rare future is not intervening to make that future
> happen.**

An ICP carrier claim requires a physical operation that changes the path law,
not merely a postselected subset whose conditional statistics resemble another
process.

## 6. Entropy production is not stored constraint

Jarzynski, Crooks, and Seifert connect work or entropy production to ratios of
forward and reverse path probabilities under specific nonequilibrium and
microscopic-reversibility assumptions (`S071`–`S073`). These results expose
time-asymmetry in a path ensemble. They do not by themselves measure how much
predictive organization a system stores.

Still et al. prove a sharper connection in a specified driven stochastic setup:
nonpredictive information is tied to thermodynamic inefficiency (`S074`). This
is important evidence that predictive organization can have energetic
consequences. It remains conditional on the model, preparation, and driving
protocol; it is not a universal identity between “information,” memory,
entropy production, and ICP constraint.

Thus:

- entropy production concerns path-law irreversibility or dissipation;
- entropy rate concerns randomness generation;
- excess entropy concerns past–future dependence; and
- statistical complexity concerns predictive-state memory.

They can move independently.

## 7. Relative entropy and allowed operations

Relative entropy is not just another uncertainty score. It measures a directed
distinguishability from a reference state or distribution. Its contraction
under an allowed channel—data processing—makes the operation family
constitutive (`S085`).

For a chosen channel family `O`, resource monotones inherit the prohibition:
an allowed operation cannot increase the declared distinguishability or
resource measure. This is deeply aligned with ICP's concern for restricted
futures, but the native theory already supplies the order. ICP adds science only
if it predicts a stable carrier, new order relation, or new operational
discriminator beyond that theory.

## 8. One-shot entropy and task dependence

Asymptotic Shannon or von Neumann entropy is often the wrong quantity for a
single finite system. Conditional min- and max-entropies have operational roles
in guessing, privacy amplification, compression, and decoupling with explicit
error tolerances (`S086`). Different tasks inspect different tails of the same
state.

Consequently:

- “the entropy” is incomplete without the task and smoothing tolerance;
- finite-resource accessibility can require a family of entropic quantities;
  and
- equality of asymptotic entropy does not imply equality of one-shot futures.

## 9. Transformation preorders: one scalar is often insufficient

Nielsen's theorem characterizes deterministic pure-state entanglement
transformations under LOCC through majorization (`S087`). Equal entanglement
entropy does not generally determine comparability: the ordered vector of
Schmidt coefficients matters.

In nanoscale thermodynamics, Brandão et al. obtain families of generalized free
energies for catalytic thermal operations on block-diagonal states (`S088`).
Lostaglio et al. show that even those free-energy constraints are insufficient
when coherence across energy eigenspaces matters; independent time-translation
asymmetry constraints are required (`S089`).

Wilming, Gallego, and Eisert make control itself explicit: restricting the
available Hamiltonians changes maximum extractable work even when the state is
held fixed (`S092`). The current frontier result of Lie et al., published 13
July 2026, characterizes thermal operations by “informational equilibrium” at
the channel-dilation level (`S093`). It is especially relevant to ICP because a
channel constraint precedes its state-conversion monotones. It remains a result
about a specified quantum-channel class, not a universal derivation of ICP.

This supplies one of the strongest entropy lessons for ICP:

> **A physical constraint is often a partial order on transformations. A
> scalar entropy is at most one monotone of that order, and sometimes an entire
> familiar family is still incomplete.**

The declared operation class—LOCC, thermal operations, catalytic operations,
covariant channels, or another family—is not a technical footnote. Change it
and the possible futures change.

## 10. Quantum entropy depends on the observable algebra

Von Neumann entropy requires a state on a declared subsystem or algebra. In
gauge theories, physical-state constraints can obstruct a simple tensor-product
factorization. Boundary flux sectors and centers contribute entropy terms, and
different algebra or edge-mode prescriptions can assign different entropies to
what is informally called the same region (`S090`, `S091`).

Two 2026 frontier sources sharpen the same warning without settling quantum
gravity. Klinger, Kudler-Flam, and Satishchandran argue in a preprint that a
more complete horizon symmetry/edge-mode algebra adds an infinite constraint
family and changes the algebraic generalized entropy (`S094`). Han's
peer-reviewed loop-quantum-gravity calculation derives an area-leading entropy
for a declared fixed-area algebra, while constraint choices survive in sector
and subleading terms (`S095`). A shared leading area law is therefore not a
unique signature of a shared constraint mechanism.

This reinforces the black-hole result. Entropy must be indexed by the
observable algebra `A`; an unqualified statement that “information is in the
region” is not operationally complete. Relative entropy and mutual information
can be more robust than the individual algebra-dependent entropy, but they too
require declared algebras and states.

## 11. Rényi, Tsallis, and algorithmic quantities

Rényi entropies form a family that changes sensitivity to different portions of
a distribution and includes Shannon entropy as a limit (`S082`). Tsallis
entropy supplies a nonadditive family used in generalized-statistical models
(`S083`). These choices can be mathematically and empirically useful, but
selecting an index or fitting a non-Shannon form does not identify the physical
mechanism that constrained the system.

Kolmogorov complexity asks for the shortest program producing an individual
object rather than an ensemble uncertainty (`S084`). It can express descriptive
regularity in a single history, but exact complexity is uncomputable and depends
on a reference machine up to an additive constant. Compressor length is only an
upper-bound proxy. Algorithmic complexity must not be silently equated with
thermodynamic entropy, predictive memory, or computational cost.

The general rule is:

> **Choose an entropy because its operational theorem matches the scientific
> task, not because its curve looks favorable to ICP.**

## 12. An entropy profile for constrained futures

No finite profile is complete, but the following prevents several common
collapses. For each matched state `m`, intervention `pi`, algebra `A`, and
boundary `B`, report where applicable:

`K_tau^pi = (V_tau, h_top, h_mu, E, C_mu, I_pi(.), Sigma, {M_j})`,

where:

- `V_tau = log mu(Gamma_tau^pi)` is finite-horizon support volume under a
  declared topology and measure;
- `h_top` is distinguishable path-support growth;
- `h_mu` is typical randomness production per step;
- `E` is past–future predictive information;
- `C_mu` is minimal predictive-state memory in the chosen model class;
- `I_pi(.)` is a rare-event rate function;
- `Sigma` is entropy production for a declared forward/reverse experiment; and
- `{M_j}` is the necessary monotone family for the allowed-operation preorder.

The full support language, transition graph, state-conversion order, and
observable algebra must remain available beside the profile. Equal profiles do
not prove equal future structures.

## 13. Empirical design for an ICP entropy test

The first useful experiment is not “measure whether entropy goes down.” It is:

1. **Declare the object.** Freeze the system boundary, state variables,
   observation algebra, topology, reference measure, horizon, and operation
   family.
2. **Match the present.** Prepare histories that agree on the best available
   present macrostate but differ in the proposed embodied record.
3. **Manipulate the carrier.** Randomize, erase, perturb, or transplant the
   candidate record with energy, material, and sham controls.
4. **Estimate the future law.** Compare held-out path distributions under a
   preregistered intervention family.
5. **Decompose the difference.** Ask separately whether support, weights,
   predictive memory, rare-event costs, dissipation, or allowed transformations
   changed.
6. **Enlarge the state.** Test whether a standard state augmentation or hidden
   variable removes the apparent history dependence.
7. **Test representation stability.** Repeat across justified partitions,
   algebras, resolutions, and entropy functionals selected before inspecting
   the result.
8. **Demand novel content.** Compare with the full native dynamical,
   resource-theoretic, or statistical model.

An ICP entropy claim fails if the proposed carrier manipulation produces no
replicable future-law difference, or if all differences are accounted for by a
better specified ordinary state and dynamics.

## 14. Mandatory non-equivalences

- State-count restriction != distributional reweighting.
- Physical constraint != constraint in a variational inference.
- Shannon entropy != thermodynamic entropy.
- One-symbol entropy != entropy rate.
- Entropy rate != predictive information.
- Predictive information != statistical complexity.
- Topological entropy != metric/KS entropy.
- Entropy production != stored predictive organization.
- Rare-event conditioning != causal intervention.
- von Neumann entropy != a partition-independent regional property.
- Equal entropy != mutual convertibility under allowed operations.
- Free-energy decrease != complete quantum-thermodynamic accessibility.
- Rényi or Tsallis index choice != physical mechanism.
- Kolmogorov complexity != a computable empirical entropy.
- Lower entropy != more organization without a task-specific organization
  measure.

## 15. What this does—and does not—do for ICP

### Established results

Mature fields already establish state counting, coding entropy, entropy rates,
dynamical entropies, fluctuation relations, data processing, one-shot tasks,
majorization orders, generalized free-energy constraints, and algebra-relative
quantum entropy within their stated regimes.

### Supported synthesis

Across those fields, constraint appears first in a compatible set, probability
law, path language, observable algebra, reference state, or operation preorder.
Entropy is derived from or monotone under that structure. A scalar is generally
not sufficient to recover it.

### ICP hypothesis

A physically embodied record may be a manipulable state variable that changes
the intervention-indexed future-law family, with a reproducible signature in
one or more entropy-profile components.

### Novelty burden

ICP is not established by rephrasing the second law, MaxEnt, data processing,
majorization, computational mechanics, or resource theory. It must provide an
additional invariant, prohibition, compression, or held-out carrier response
that those complete native accounts do not already provide.

### Present conclusion

Entropy does not replace the Information–Constraint Principle, and ICP should
not be renamed after an entropy. Entropy gives the project a mature family of
operational probes and no-go constraints. The principle's distinctive target
remains the physically embodied structure that differentiates counterfactual
future laws.
