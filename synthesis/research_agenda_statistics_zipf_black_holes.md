# ICP research expansion: statistics, Zipf, and black-hole information

- Date scoped: 2026-07-19
- Status: research agenda; sources below are candidates pending protocol-based
  screening and extraction
- Governing constraint: preserve the original seven-pillar first-paper
  architecture

## Editorial decision

These topics belong to one research program but not at the same structural
level:

1. **Statistics of future ensembles** is shared formal infrastructure for all
   seven pillars.
2. **Zipf's law** is a worked mechanism-discrimination case at the junction of
   computational mechanics and statistical emergence.
3. **Black-hole information** is a frontier stress test spanning quantum
   persistence, memory, relational observables, encoding, and recoverability.

Paper 1 should contain the formal language plus one compact box for Zipf and one
frontier box for black-hole information. Full treatments belong in follow-on
papers so the initial synthesis remains coherent and defensible.

## 1. Statistics as the geometry of constrained futures

### 1.1 Core object

For a realized history `H_t`, a proposed present physical record `M_t`, an
admissible policy or intervention `pi`, and future horizon `tau`, study the path
law

`P^pi_H(F[t:t+tau] | M_t)`.

The whole ICP object is not one forecast but a family of future laws over the
allowed intervention set `Pi`:

`E_t = {P^pi_H : pi in Pi}`.

This family separates:

- **hard accessibility:** `R^pi_tau(H) = support(P^pi_H)`;
- **soft constraint:** probability weights within `R^pi_tau`;
- **predictive equivalence:** histories giving the same future distribution;
- **intervention equivalence:** histories giving the same future distribution
  for every admissible intervention;
- **resource-relative accessibility:** futures distinguishable, controllable,
  reconstructable, or computable with declared resources.

In continuous path spaces, individual trajectories normally have probability
zero. Impossibility must therefore be defined through support, neighborhoods,
or dynamical reachability—not by zero point probability or an arbitrary
confidence region.

### 1.2 Terminology that must remain separate

- Predictive: `P(F | H = h)`.
- Interventional: `P(F | do(pi), H = h)`.
- Counterfactual or potential trajectory: `F^pi`, asking what the same modeled
  unit would have done under `pi`.
- Joint comparison of `F^pi` and `F^pi'`: requires a structural coupling or
  potential-outcome model; it is not identified by the two marginal
  interventional distributions alone.

Alternate stochastic realizations under one unchanged law are possible futures,
not automatically counterfactual futures. Computational-mechanics causal states
are predictive equivalence classes; their name does not by itself supply
intervention semantics.

### 1.3 Candidate formal tools

- stochastic processes and path-space measures;
- predictive information and entropy rate;
- computational-mechanics causal states and statistical complexity;
- predictive-state representations and controlled input-output processes;
- Maximum Caliber and constrained path ensembles;
- large-deviation rate functions and conditioned rare-event processes;
- control-theoretic reachability and viability;
- structural causal models and potential outcomes;
- process tensors and quantum instruments;
- total-variation, Wasserstein, or relative-entropy comparisons between future
  laws, always with an explicit reference and operational meaning.

A natural but not yet novel ICP candidate is intervention-aware equivalence:

`h ~_(Pi,A) h' iff every allowed future instrument in observable algebra A has the same outcome distribution under h and h' for every pi in Pi`.

This is close to predictive-state, input-output computational-mechanics, control,
and quantum-process formalisms. ICP needs an additional theorem, invariant,
physical embodiment criterion, or empirical discriminator before claiming it as
new.

### 1.4 The strongest operational experiment

1. Prepare systems with the same declared present macrostate but different
   histories.
2. Apply the same randomized interventions.
3. Compare their out-of-sample future path laws.
4. Progressively enlarge the state description.
5. Identify a proposed physical record `M_t`.
6. Erase, replace, or perturb `M_t` while controlling material, energetic,
   geometric, and boundary variables.

If the history effect disappears under adequate state augmentation, the result
supports the incomplete-state null. If a specified physical record predicts and
mediates the difference under intervention, ICP gains operational content.

### 1.5 Seed primary sources

- [Pearl (1995), causal diagrams and interventions](https://proceedings.mlr.press/r0/pearl95a.html)
- [Rubin (1974), potential outcomes](https://doi.org/10.1037/h0037350)
- [Shalizi and Crutchfield, computational mechanics](https://arxiv.org/abs/cond-mat/9907176)
- [Bialek, Nemenman, and Tishby, predictive information](https://arxiv.org/abs/physics/0007070)
- [Ge et al., Markov processes from Maximum Caliber](https://arxiv.org/abs/1106.4212)
- [Chetrite and Touchette, conditioned rare events and driven processes](https://arxiv.org/abs/1405.5157)

## 2. Zipf as a discriminating ICP laboratory

### 2.1 Why Zipf matters

A Zipfian rank-frequency relation, approximately `f(r) proportional to r^-alpha`
with `alpha` near one in some systems, is an unusually strong test of scientific
discipline. Similar marginals can arise from incompatible mechanisms. The law
therefore cannot by itself show that history has constrained future
accessibility.

The useful ICP question is not, "Does constraint produce Zipf?" It is:

> Which history-dependent physical mechanism, if any, generates both the
> observed rank-frequency marginal and a distinctive conditional distribution
> over future events or innovations?

### 2.2 Rival mechanisms that must be compared

- preferential growth or Yule-Simon processes;
- latent-variable and mixture models;
- random typing or random segmentation;
- least-effort and communicative optimization;
- maximum-entropy models under chosen constraints;
- critical or near-critical organization;
- sample-space-reducing and other history-dependent processes;
- finite-size, sampling, aggregation, and spurious-scaling effects.

Sample-space reduction is a particularly literal ICP bridge, but it must not be
privileged merely because its language resembles constraint. Mechanisms must be
discriminated by predictions beyond the fitted exponent.

### 2.3 First analysis design

1. Predefine the token, type, sequence, boundary rules, and sampling frame.
2. Fit the tail with likelihood-based estimation and goodness-of-fit tests;
   compare power law, lognormal, stretched exponential, and mechanistic rivals.
3. Shuffle the observed sequence. Shuffling preserves the rank-frequency
   marginal while destroying temporal organization. Any proposed ICP statistic
   that cannot distinguish the original from the shuffle measures only the
   marginal.
4. Fit iid heavy-tail, preferential-growth, latent-mixture, finite-state or
   grammar, and history-reducing models.
5. Compare out-of-sample sequential likelihood, successor distributions,
   predictive information, causal states, path entropy, innovation rate, and
   relaxation after perturbation.
6. Require a mechanism-specific prediction or intervention response beyond
   Zipf's exponent.

### 2.4 Seed primary and methods sources

- [Simon (1955), stochastic growth mechanism](https://doi.org/10.1093/biomet/42.3-4.425)
- [Schwab, Nemenman, and Mehta (2014), latent variables and apparent criticality](https://arxiv.org/abs/1310.0448)
- [Corominas-Murtra, Hanel, and Thurner, history-dependent sample-space reduction](https://arxiv.org/abs/1407.2775)
- [De Marzo et al. (2021), dynamical versus spurious Zipf behavior](https://doi.org/10.1103/PhysRevResearch.3.013084)
- [Clauset, Shalizi, and Newman, power-law model testing](https://doi.org/10.1137/070710111)
- [Prossillo, Hébert-Dufresne, and Dodds (2026), finite type-token/rank relationships](https://doi.org/10.1103/q9w5-7k3j)

## 3. Quantum and black-hole information

### 3.1 Why this is a frontier test

Black-hole information theory forces four notions apart:

1. information present in a global quantum state;
2. information distinguishable relative to an observable algebra;
3. information reconstructable from a subsystem or code;
4. information efficiently recoverable with finite computational and physical
   resources.

This is highly relevant to ICP because persistence and accessibility can diverge
sharply. It is not direct evidence for ICP, and controlled model results must not
be generalized to astrophysical evaporation without an explicit bridge.

### 3.2 Core formal objects

- Page curve: time dependence of radiation entropy expected under a unitary
  random-state model;
- generalized entropy: area term plus bulk quantum entropy and counterterms;
- quantum extremal surfaces and entanglement islands;
- replica-wormhole saddles in gravitational entropy calculations;
- entanglement-wedge reconstruction and operator-algebra quantum error
  correction;
- scrambling time, decoding channel, and computational complexity;
- factorization and completeness of gravitational observable algebras.

An ICP mapping to test, not assume, is:

- `H`: formation, infall, interactions, and evaporation history;
- `M`: nonlocal correlations, code subspace, geometry, or algebraic encoding;
- `Pi`: allowed measurements, couplings, collection protocols, and decoding
  operations;
- `F`: future measurement statistics and recoverable observables.

A Page transition is a change in an entropy extremization or reconstruction
description, not a literal branching of physical futures. Generalized entropy is
not a counterfactual-future measure. Replica wormholes are Euclidean saddles, not
automatically real-time information carriers.

### 3.3 Status ladder

Relatively controlled results include Page's random-state calculation,
quantum-extremal-surface and entanglement-wedge results in stated holographic
regimes, and island/Page-curve calculations in JT gravity, AdS/CFT with baths,
random-matrix models, and related code or braneworld settings.

Not established for a collapsing, rotating, asymptotically flat astrophysical
black hole are the complete evaporation mechanism, microscopic carrier of
recovered information, operational feasibility of decoding, or a unique
resolution of factorization, firewall, remnant, fuzzball, and state-dependence
questions. No astronomical measurement has detected the information-bearing
correlations of Hawking radiation.

### 3.4 Current frontier to track through 2026-07-19

- [Colafranceschi et al., algebraic entropy from gravitational path integrals](https://arxiv.org/abs/2310.02189)
  strengthens the observable-algebra framing under explicit gravitational-path-
  integral axioms.
- [Geng, Karch-Randall replica wormholes and islands](https://arxiv.org/abs/2405.14872)
  connects the replica-wormhole saddle to an RT-surface transition in a
  controlled braneworld with a nongravitating bath.
- [Matsuo, universal structure of islands in evaporating black holes](https://doi.org/10.1007/JHEP03%282025%29068)
  studies the location of quantum extremal surfaces across general model
  classes.
- [Antonini et al., An apologia for islands](https://arxiv.org/abs/2506.04311)
  argues for islands and observable Page curves with massless gravity and no
  external reservoir in several settings.
- [Geng, mechanism behind information encoding for islands](https://doi.org/10.1007/JHEP03%282026%29037)
  argues that the local encoding mechanism in standard island models depends
  essentially on massive-gravity physics.
- [Geng et al., Seeing Page Curves and Islands with Blinders On](https://arxiv.org/abs/2602.06543)
  argues that complete asymptotic observable algebras already contain interior
  information and that nontrivial Page curves require restricted access or a
  nongravitating bath.

The massless-gravity, factorization, and asymptotic-algebra debate is active. It
should be represented as a live disagreement, not collapsed into consensus.

### 3.5 Foundational seed sources

- [Page, information in black-hole radiation](https://arxiv.org/abs/hep-th/9306083)
- [Engelhardt and Wall, quantum extremal surfaces](https://arxiv.org/abs/1408.3203)
- [Penington, entanglement-wedge reconstruction and the information paradox](https://arxiv.org/abs/1905.08255)
- [Almheiri et al., entropy and the entanglement wedge of an evaporating black hole](https://arxiv.org/abs/1905.08762)
- [Almheiri et al., replica wormholes and Hawking-radiation entropy](https://arxiv.org/abs/1911.12333)
- [Penington et al., replica wormholes and the black-hole interior](https://arxiv.org/abs/1911.11977)
- [Almheiri, Dong, and Harlow, bulk locality and quantum error correction](https://arxiv.org/abs/1411.7041)
- [Hayden and Preskill, black holes as mirrors](https://arxiv.org/abs/0708.4025)
- [Harlow and Hayden, computational limits on decoding Hawking radiation](https://arxiv.org/abs/1301.4504)

## 4. Recommended publication sequence

### Paper 1 — ICP foundations

**Information as Constraint on Physical Possibility: A Critical
Cross-Disciplinary Synthesis**

Retain all seven original pillars, add the common future-ensemble language, and
use short Zipf and black-hole frontier boxes.

### Paper 2 — statistical formalization and Zipf stress test

**The Statistics of Constrained Futures: Predictive, Interventional, and
Path-Ensemble Foundations for ICP**

Develop the mathematical framework and use Zipf to discriminate marginal pattern
from history-dependent mechanism.

### Paper 3 — quantum-gravitational frontier

**Information, Accessibility, and Constrained Futures in Black-Hole Physics**

Compare generalized entropy, islands, observable algebras, quantum error
correction, scrambling, and resource-bounded recovery without claiming that
controlled models settle astrophysical information loss.

## 5. Immediate next steps

1. Register and screen the seed sources rather than treating this agenda as an
   evidence table.
2. Draft the common comparison-table schema with `H, M, Pi, P^pi, R^pi`,
   observable algebra, resource bound, and strongest non-equivalence.
3. Select one sequence-bearing Zipf dataset with a meaningful intervention or
   perturbation model.
4. Build the Zipf rival-model and shuffle-control analysis before interpreting
   any exponent.
5. Extract the 2025–2026 black-hole disagreement as paired claims with exact
   assumptions and observable algebras.
6. Keep all conclusions graded as field result, synthesis inference, or ICP
   hypothesis.
