# Pilot Batch 03 — Information, accessibility, and constrained futures in black-hole physics

- Date: 2026-07-19
- Protocol: 0.4
- Scope: information loss, Page curves, decoding, QES/islands, replica
  wormholes, holographic error correction, observable algebras, and the
  massless-gravity dispute
- Independent literature base: 27 primary or primary-adjacent sources
  (`S039`–`S065`), including 23 peer-reviewed papers and four explicitly
  labeled preprints
- Current-search cutoff: 2026-07-19; latest retained sources are June 2026
- Status: frontier stress test, not evidence that an ICP ontology is true and
  not an exhaustive review of every proposed resolution

## Outcome first

Black-hole information theory improves ICP by forcing one word—“information”—
into at least five operationally different claims:

1. two preparations remain distinct in the global quantum state;
2. a declared observable algebra can distinguish them;
3. a logical algebra can be reconstructed on a chosen subsystem;
4. a decoder can recover a specified message or reference correlation;
5. that decoder can be executed within stated time, precision, energy, copy,
   and computational limits.

None of the converse implications is automatic. Global preservation does not
imply local access. Reconstruction does not imply an efficient decoder. A Page
curve does not identify a microscopic channel, a carrier, or the moment when
information literally travels across a horizon. A Euclidean replica-wormhole
saddle is not by itself a real-time memory mechanism.

The central non-equivalence is therefore:

> **The same Page-shaped entropy curve does not imply the same carrier,
> channel, observable algebra, reconstruction map, or recovery cost.**

This is the black-hole analogue of the Zipf result. Zipf showed that one
marginal can have incompatible causes. Black-hole theory shows that even the
statement “the information is outside” can change when the subsystem,
observable algebra, or resource budget changes.

The most defensible ICP contribution is not another solution to the information
paradox. It is a discipline for indexing future-law claims by operations,
observables, and resources and for refusing to collapse preservation,
distinguishability, reconstruction, recovery, and efficient recovery.

## 1. Native problem and conditional benchmarks

Hawking's semiclassical argument replaces a unitary S-matrix with a
superscattering map capable of pure-to-mixed evolution. Its conclusion depends
on tracing over an inaccessible hidden region and on the assumed completeness
of the exterior description (`S039`).

Page asks a different, conditional question: **if** formation and evaporation
are unitary and the black-hole/radiation state is typical, what entropy should a
chosen radiation subsystem have? The resulting curve is a random-state
benchmark, not a derivation of black-hole dynamics (`S040`).

Hayden and Preskill add a recovery task: under unitary rapid mixing and ideal
control of early radiation, a message thrown into an old black hole becomes
recoverable after little additional radiation (`S041`). Harlow and Hayden then
show why “recoverable in principle” may still be operationally unavailable: a
generic AMPS decoder can require time exponential in black-hole entropy
(`S044`).

Mathur's small-corrections theorem and the AMPS trilemma constrain proposals
rather than selecting one. Unspecified perturbatively small corrections do not
reverse Hawking entanglement under Mathur's premises; radiation purity,
ordinary exterior EFT, and a smooth horizon cannot all survive the AMPS
factorization assumptions (`S042`, `S043`).

These results already require three different outcome types:

- entropy or purity of a reduced state;
- recovery fidelity for a reference-entangled message;
- complexity or physical cost of the recovery operation.

They must not be reported as interchangeable evidence.

## 2. Operational hierarchy for ICP

Retain the project core

`E_tau(m; Pi, A, B) = {P^pi_A(F[0:tau] | m, B) : pi in Pi}`,

where `m` indexes a preparation or present encoded state, `Pi` is the allowed
operation family, `A` is the observable algebra, and `B` states physical and
computational resources.

For preparations `m` and `m'`, define an operational separation

`Delta_tau(m,m'; Pi,A,B) = sup_pi TV(P^pi_A(.|m,B), P^pi_A(.|m',B))`.

The two preparations are equivalent for that experiment only when `Delta_tau`
is below a declared tolerance. In a quantum formulation, suitable restricted
trace norms, channel norms, or hypothesis-testing quantities can replace total
variation.

### 2.1 Five claims and their witnesses

| Claim | Appropriate witness | What the witness does not establish |
|---|---|---|
| Global preservation | global trace distance; reference entanglement; isometric total channel | access by any exterior observer |
| Algebra-relative distinguishability | supremum of expectation differences over `O in A` | full logical reconstruction |
| Reconstruction | logical `O` has an `O_R` acting equivalently on a declared code subspace | full-state or state-independent decoding |
| Recoverability | a decoder achieves bounded diamond error or high entanglement fidelity | feasible execution |
| Efficient recovery | minimum gates, time, energy, copies, and precision lie inside `B` | observer-independent localization |

For full-message recovery, the safe direction is

`efficient recovery => allowed recovery => full logical-algebra reconstruction => some algebra-relative distinguishability => global distinction`.

The reverse arrows do not generally hold. Reconstruction of only a subalgebra
is weaker again.

### 2.2 Resource declaration

`B` must freeze at least:

- spacetime and boundary conditions, including any nongravitating bath;
- factorization or observable-algebra choice;
- code subspace and semiclassical order;
- collection loss and time band;
- number of identically prepared copies;
- detector precision and allowed backreaction;
- decoder knowledge, gates, runtime, energy, and error tolerance.

Without these declarations, “available,” “encoded,” and “recoverable” are not
scientific claims with a stable truth value.

## 3. QES, islands, and reconstruction: what is controlled

Engelhardt and Wall propose extremizing generalized entropy,

`S_gen = Area(partial I)/(4 G_N) + S_bulk(R union I) + counterterms`,

to obtain a quantum extremal surface (`S046`). Operator-algebra QEC and bulk–
boundary relative-entropy results explain how one logical bulk algebra can be
reconstructed on different boundary regions inside a restricted code space
(`S047`, `S048`).

In explicit evaporation models:

- Penington obtains a Page-time QES transition for an AdS/CFT black hole with
  absorbing boundary conditions; part of the interior becomes reconstructable
  from radiation (`S051`).
- Almheiri, Engelhardt, Marolf, and Maxfield obtain a related transition and
  scrambling-time behavior in a two-dimensional JT/CFT system coupled to an
  auxiliary heat sink (`S052`).
- Almheiri et al. and Penington et al. derive island behavior from connected
  replica saddles in controlled models; the latter explicitly discusses an
  ensemble-average interpretation (`S053`, `S054`).
- Geng connects replica-wormhole formation on a Karch–Randall brane to a
  higher-dimensional RT transition (`S058`).
- Matsuo derives broad near-horizon QES-location behavior within a declared
  semiclassical class (`S059`).

These are substantial theoretical results. Their proper status is nevertheless
bounded:

1. the strongest calculations use AdS/CFT, JT gravity, baths, braneworlds,
   random matrices, SYK-related models, or restricted code subspaces;
2. the replica calculation requires topology sums, saddle dominance, and
   analytic continuation;
3. the entropy curve is not a full microscopic radiation channel;
4. reconstruction existence is not efficient decoding;
5. no source in this batch directly measures information-bearing correlations
   in Hawking radiation from an astrophysical black hole.

There is no nonperturbative single-theory evaporation channel here for a
realistic four-dimensional black hole, no Level-5 efficient decoder for such a
system, and no laboratory or astronomical confirmation of its Page curve.

## 4. The observable-algebra fault line

Gravity complicates the ordinary factorization into independent spatial
subsystems. Gravitational dressing, constraints, and asymptotic charges can
make information available to a larger exterior algebra even when a smaller
“radiation” algebra does not contain it.

Raju argues that the QFT split property fails in gravity and that a complete
asymptotic algebra can determine the full state (`S056`). Colafranceschi et al.
derive boundary algebras and their entropies from a gravitational path integral
under explicit AdS and positivity axioms (`S057`). Geng et al. argue that
long-range gravitational dressing creates a Gauss-law obstacle to compact
islands (`S055`).

The current disagreement is unusually sharp:

- Antonini et al. (`S060`) define proper radiation subalgebras in massless
  gravity, argue that their entropies follow Page curves, and construct
  compactly supported gauge-invariant operators perturbatively around generic
  backgrounds without isometries.
- Geng et al. (`S063`) answer that the complete asymptotic algebra, including
  the Hamiltonian, already contains the interior information; removing it or
  using a detector with a blind region produces a restricted-access Page curve,
  not fundamental information emergence. They also dispute that approximate
  relational algebras define the needed exact fine-grained factorization.

The disagreement is partly substantive and partly about the object being
called an island or radiation entropy. They agree that an algebra must be
selected and that nongravitating-bath models produce controlled Page curves.
They disagree about whether proper subalgebras in standard massless gravity
capture the physically relevant radiation question and whether perturbative
relational operators suffice for exact fine-grained reconstruction.

Two June-2026 papers sharpen but do not settle the question. Kumar constructs a
healthy local massless-graviton wedge model whose added unitary defect entropy
supports a non-horizon late saddle, but does not give a full global
backreacted/operator-algebra solution (`S064`). Dar, Kajuri, and Panigrahi prove
right-moving asymptotic recovery in a CGHS model under holography-of-information
assumptions and argue that an island conflicts with commuting left/right
algebras, but the result is two-dimensional and lacks a full RST evaporation
and replica derivation (`S065`).

ICP should not adjudicate this dispute by renaming both sides “constraint.” Its
useful move is to record the two claims as different tuples `(A,B)` and ask
which future experiments or reconstruction tasks each algebra actually
supports.

## 5. Candidate carriers and mandatory rivals

### 5.1 Nonlocal radiation correlations

Unitary/random-state models permit information in high-order correlations.
Their rivals are nonunitary evolution, remnants, hidden sectors, or structured
non-Haar dynamics. Entropy alone does not identify the channel.

### 5.2 Code and entanglement-wedge encoding

Holographic QEC gives precise redundant reconstruction on a code subspace. The
rivals are full-Hilbert-space failure, state dependence, ensemble averaging,
and computational inaccessibility. A code is a relation among operator
representations, not automatically a material memory object localized on the
QES.

### 5.3 Massive-gravity/bath dressing

Geng's 2026 mechanism paper traces island encoding in standard bath models to
broken diffeomorphism symmetry and Goldstone/Stückelberg dressing (`S062`). This
is the closest source in the batch to a specified carrier/mediation mechanism.
Its limitation is equally important: it explains a class of massive-gravity
open systems, not yet isolated massless astrophysical gravity.

### 5.4 State-dependent reconstruction

Papadodimas and Raju construct interior operators using a state-dependent map
within an equilibrium neighborhood (`S045`). This is a serious alternative to
one state-independent carrier map over the full Hilbert space and makes the
code/preparation dependence explicit.

### 5.5 Soft hair

Hawking, Perry, and Strominger identify infinitely many soft charges and exact
conservation relations (`S049`). Mirbabayi and Porrati show why this does not
yet solve the hard-state information problem: after suitable infrared
dressing, the soft S-matrix sector can factorize essentially trivially
(`S050`). Capacity and message-recovery tests are mandatory.

### 5.6 Other resolutions

Firewalls, fuzzballs, remnants, final-state projection, and other proposals
remain important rivals. This pilot records their role in the rival matrix but
does not claim an exhaustive source extraction for each program. Mathur's
paper supplies the small-corrections gate and a programmatic fuzzball case;
AMPS supplies a consistency constraint, not a carrier proposal.

## 6. ICP mapping and counterfactual discipline

For a black-hole application:

- `H`: collapse, initial microstate, infall, interactions, and evaporation
  history;
- `M`: the complete present gravitational/matter state or a proposed encoding
  such as radiation correlations, a code embedding, dressing, soft sector, or
  remnant;
- `Pi`: couplings to a bath, collection protocols, detector placements,
  erasures, decoding channels, and controlled diary insertions;
- `A`: the bath, radiation, boundary-subregion, asymptotic, relational, or
  global observable algebra;
- `B`: semiclassical order, copies, precision, time, energy, and computational
  budget;
- `F`: future measurement statistics, recovery fidelity, reconstructed logical
  observables, and resource cost.

A Page transition is a change in the minimizing generalized-entropy saddle or
reconstruction assignment. It is not automatically a branching or pruning of
physical counterfactual futures. Replica geometries are terms in a calculation,
not interventions in `Pi` unless a separate physical model makes them so.

Counterfactual comparisons require an explicit structural intervention—for
example attach versus do not attach a bath, erase different radiation
fractions, include versus blind a detector region, or vary the decoder budget—
with the same preparation relation specified across regimes. Merely comparing
two entropy curves does not identify the joint counterfactual state of one
black hole.

## 7. Discriminating experiment and calculation families

1. **Reference-entangled diary.** Inject half of an entangled pair, collect a
   declared radiation region, and score decoder entanglement fidelity while
   varying time, loss, and computational budget.
2. **Algebra sweep.** Evaluate the same preparation under nested low-order,
   time-band radiation, complete asymptotic, and global algebras. Record where
   operational distinguishability first appears.
3. **Degree-of-freedom closure.** Compare radiation alone with radiation plus
   remaining hole, bath, remnant, and hard/soft sectors before calling loss
   fundamental.
4. **Carrier intervention.** Perturb the proposed dressing, code embedding,
   soft sector, or boundary coupling while holding conserved charges and coarse
   geometry fixed as far as the model allows.
5. **Reconstruction threshold.** Vary erasure pattern, code-subspace dimension,
   bath coupling, and region size; report logical-operator error separately
   from full-channel recovery.
6. **Complexity frontier.** Report minimum resources `C_epsilon(S_BH)` for a
   target error rather than the binary word “available.”
7. **Individual-theory gate.** Require the entropy curve, multi-time channel,
   and recovery map in a fixed microscopic theory. An ensemble-averaged result
   is not silently transferred to an individual black hole.

## 8. Falsification and admission gates

A black-hole claim should count as ICP-relevant only after:

- tuple closure: `m, Pi, A, B, tau` are explicit;
- state-space closure before a claim of fundamental information loss;
- separate tests of entropy, distinguishability, reconstruction, recovery, and
  efficiency;
- at least one prediction beyond a Page-shaped curve;
- carrier necessity and sufficiency tests where a carrier is claimed;
- an observable-algebra sensitivity analysis;
- individual-theory versus ensemble-average separation;
- model-transfer discipline from random unitaries, AdS/CFT, JT+bath, and
  braneworlds to astrophysical evaporation;
- no interpretation of replica saddles as literal counterfactual futures
  without an additional causal model.

If all claimed ICP content disappears once standard quantum channel, algebra,
code-subspace, boundary, and resource variables are supplied, ICP is a useful
indexing vocabulary but not a new physical principle in this domain.

## 9. Evidence-status conclusion

### Established or controlled within stated frameworks

- Hawking's semiclassical pure-to-mixed argument under its assumptions;
- Page/random-subsystem typicality results conditional on unitarity;
- quantum-information recovery and complexity results under stated channel
  assumptions;
- QES, holographic QEC, relative-entropy, and replica/island results in their
  specified AdS/JT/bath/code regimes;
- an active, mathematically substantive dispute about the correct observable
  algebra in massless gravity.

### Not established by this literature batch

- the full microscopic evaporation channel of a realistic rotating,
  asymptotically flat black hole;
- a unique carrier of recovered information;
- an efficiently executable astrophysical decoder;
- direct observation of a Page curve or information-bearing Hawking
  correlations;
- a universal counterfactual-future measure;
- ICP as a new law of quantum gravity.

## 10. Implication for the principle and publication plan

Keep **ICP = Information–Constraint Principle**.

Black-hole theory strengthens the case that ICP is identifying a distinct
cross-domain question: what physically encoded distinctions survive for which
operations, observables, and resources, and how do those distinctions constrain
the future laws available to a system? The name states the proposed principle;
the evidence grades state how far it has been established. Those are separate
matters.

The entropy, channel, algebra, QEC, and complexity formalisms still do the native
physics. ICP earns status as an independently established physical principle
only if it provides a cross-domain theorem, invariant, prohibition, or
experiment that those formalisms do not already supply. Until then, the honest
description is **the proposed Information–Constraint Principle**, not a
different expansion of ICP.

Paper 1 should retain a bounded frontier box. A full Paper 3 can develop the
five-level hierarchy, the current algebra/island disagreement, and the
reference-diary/algebra-sweep test suite without claiming that controlled model
Page curves settle astrophysical information loss.
