# Bounded closure: quantum records, relational facts, reference frames, and causal order

**Project:** ICP literature synthesis  
**Evidence cutoff:** 2026-07-20  
**Review type:** adversarial critical-scoping closure, not a systematic review or meta-analysis  
**Scope:** decoherence/quantum Darwinism; relational quantum mechanics (RQM) versus quantum reference frames (QRFs); a deliberately compact definite/indefinite-causal-order boundary  
**Primary question:** What does established quantum science actually support about interaction-generated information becoming a physically carried, persistent constraint on later possibilities—and what does it not support?

## Executive result

This literature gives ICP a real but sharply bounded foothold.

The strongest positive result comes from decoherence and quantum Darwinism: an interaction can move correlations about a source system into distinct environmental degrees of freedom; selected observables can be encoded repeatedly; and separate observers can sometimes recover the same classical information from disjoint fragments without directly measuring the source. Controlled photonic and spin experiments have observed early forms of this record proliferation. That is genuine evidence that information about a system can persist in secondary physical carriers after the originating interaction and become operationally available away from the source.

It is **not** evidence that information exists without physical realization, that every decohering environment creates objective records, or that a record by itself changes the law governing future evolution. The relevant hierarchy is:

> decoherence ≠ einselection ≠ redundant encoding ≠ accessible consensus ≠ spectrum-broadcast objectivity ≠ inherited constraint on future possibilities.

The factorization problem is a serious boundary, not a footnote. The observable that appears redundantly recorded can depend on how the total Hilbert space is divided into system and environment. Recent work shows that a fixed Hamiltonian can admit multiple quasiclassical tensor-product structures, not necessarily aligned with familiar spatial locality. Any ICP claim based on “the record in the environment” must therefore specify the system decomposition, accessible observable algebra, allowed interventions, and the transformations under which the carrier claim remains invariant.

RQM and QRF research helps impose that discipline but does not independently validate ICP. RQM is an interpretation centered on facts actualized relative to interactions. QRF theory develops transformations among descriptions relative to physical reference systems within quantum theory. Their shared word *relational* does not make them the same theory. Neither, by itself, supplies an accumulated memory variable or predicts that changing a past-generated record while holding the current controlled state fixed changes the future process.

Indefinite-causal-order work provides a useful formal analogue: a physical control can condition which sequence of operations is available. But the scientific ladder must remain explicit:

> coherent control of gate order ≠ causal nonseparability ≠ causal-inequality violation ≠ superposition of spacetime causal structure ≠ emergence of causality from an information substrate.

The 2026 photonic causal-order result is important and should be cited, but it is a proof-of-principle violation under substantive assumptions and acknowledged loopholes, not device-independent evidence that spacetime causal structure is indefinite.

### Bottom-line verdict for the ICP synthesis

- **Supported as a field result:** correlations formed in an interaction can be embodied in secondary degrees of freedom, survive source separation, and be accessed redundantly under identifiable dynamical and measurement conditions.
- **Supported as a synthesis inference:** “persisted information” should be modeled as a physically instantiated relation among source history, carrier state, accessible observables, and intervention context—not as a free-floating substance.
- **Viable as an ICP research hypothesis:** such embodied records may constrain a later family of accessible states, transformations, or counterfactual futures.
- **Not yet established:** that the record is an additional physical state variable beyond a complete standard-physics description; that it changes future laws rather than ordinary conditional dynamics; or that information is the substrate from which mass, energy, spacetime, or causality emerge.

The decisive next step is not another analogy. It is an intervention experiment that creates the same controlled present state by different histories, then edits, erases, or exchanges the candidate record carrier and measures whether the later process family changes.

## Claim discipline used here

Three labels are kept separate throughout:

- **Field result:** a result established within the cited theory, model, theorem, or experiment, with its assumptions retained.
- **Synthesis inference:** a cross-literature interpretation useful for organizing ICP, but not itself a result reported by the source.
- **ICP hypothesis:** a new, testable claim that would require an explicit bridge experiment or derivation.

“Objective,” “record,” “fact,” “reference frame,” “causal order,” and “constraint” are not treated as interchangeable terms. In particular, an environmental degree of freedom that correlates with a source is a *candidate record carrier*. It becomes an operational record only relative to a specified readout algebra and reliability criterion. It becomes an ICP-style inherited constraint only if the record's physical status makes a discriminable difference to later reachable behavior under controlled interventions.

---

## 1. Decoherence and quantum Darwinism: the positive mechanism and its limits

### 1.1 What the positive theory actually says

Let a system \(S\) interact with an environment \(E=E_1\cdots E_N\). A schematic branching state is

\[
  |\Psi\rangle_{SE}=\sum_i c_i\,|s_i\rangle
  |\varepsilon_i^{(1)}\rangle\cdots|\varepsilon_i^{(N)}\rangle .
\]

If the conditional environment states associated with different \(i\) become sufficiently distinguishable, tracing out unobserved degrees of freedom suppresses off-diagonal terms in the reduced state of \(S\). Environment-induced superselection, or *einselection*, identifies comparatively stable pointer states/observables under the interaction. Quantum Darwinism adds a further claim: many disjoint fragments can carry usable information about the same pointer observable, allowing multiple observers to infer it indirectly.

Ollivier, Poulin, and Zurek made this “environment as witness” mechanism precise: the environment does not merely decohere the system; it can selectively proliferate information about preferred observables. Brandão, Piani, and Horodecki later proved a broad channel result. For a channel from a finite-dimensional system into many environmental components, most small reduced fragment channels are approximately measure-and-prepare channels for one common system POVM. In that asymptotic and channel-defined sense, many observers obtain at most classical information about the same observable.

The theorem is strong, but its exact content matters. A measure-and-prepare form

\[
  \mathcal{E}_j(\rho)=\sum_k \operatorname{Tr}(M_k\rho)\,\sigma_{j,k}
\]

does not by itself guarantee that every observer can distinguish all \(k\), that different fragments contain full copies of the outcome, or that the relevant system/environment decomposition is unique. It establishes generic classicalization of the *observable information available through most local fragment channels*, not generic perfect broadcast of objective outcomes.

### 1.2 The objectivity ladder

| Level | Operational content | What is still missing |
|---|---|---|
| Decoherence | Interference is suppressed in a reduced description because phase information is dispersed into correlations. | A unique outcome, a stable pointer observable, accessible copies, or observer consensus. |
| Einselection | The dynamics selects observables/states robust under environmental monitoring. | Redundant or independently readable records. |
| Quantum-Darwinist redundancy | Many fragments contain information about a common system observable, often diagnosed by mutual-information plateaus. | Proof that the information is classical, locally accessible, independently readable, and non-disturbing. |
| Strong quantum Darwinism | The fragment information is the relevant classically accessible information with suppressed discord, under the stated measure. | Conditional independence among records. |
| Spectrum broadcast structure (SBS) | Approximately \(\rho_{SE}=\sum_i p_i|i\rangle\langle i|\otimes\rho_i^{E_1}\otimes\cdots\), with orthogonal conditional supports in each observed fragment. | Uniqueness across decompositions; a law-like role for the records in later dynamics. |
| ICP inherited constraint | A past-generated, embodied record discriminably changes later accessible transformations or counterfactual futures under a controlled intervention. | This is not delivered by decoherence or QD and must be independently tested. |

Horodecki, Korbicz, and Horodecki introduced SBS as a stringent state structure for objective information: disjoint observers can identify the same index without perturbing the system or one another's records because conditional fragment states have orthogonal supports. Le and Olaya-Castro related strong quantum Darwinism plus a strong-independence condition to SBS. That equivalence must be cited with the subsequent correction: Feller and collaborators showed that the originally used pairwise conditional-independence condition was necessary but not sufficient for full multipartite independence; the corrected, stronger condition is required.

Two additional distinctions are central for ICP:

1. A quantum mutual-information plateau can occur even when the relevant information is not locally accessible classical information and the joint state lacks SBS. Therefore, a plateau alone is not an objectivity certificate.
2. Redundancy and consensus are not identical. Nonlocally encoded information can make many observers agree under one operational definition without giving each fragment an independent copy, or can produce redundancy without the same consensus property. The carrier architecture must be specified.

### 1.3 Experiments: what has and has not been observed

Three experimental lines supply the clearest evidence.

**Engineered photonic records.** Ciampini and collaborators prepared photonic cluster/graph-state resources and reconstructed how information about a system qubit was distributed among environment qubits. The work exhibited a quantum-Darwinist signature and showed that multipartite environmental correlations and back-action can materially change it. Chen and collaborators used a six-photon simulator to observe redundancy of classical information accompanied by suppression of quantum correlations in fragments.

**A naturally coupled spin environment.** Unden and collaborators treated an NV-center electron spin as the system and nearby \(^{13}\mathrm{C}\) nuclear spins as its environment. With dynamical-decoupling control and spin-resolved readout, they observed redundant imprints of system information during decoherence—appropriately described by the authors as *incipient* classical objectivity.

These experiments are real demonstrations of carrier-separated correlations. They are also small, carefully controlled quantum simulators or few-spin environments reconstructed with substantial model and measurement access. They do not show that ordinary macroscopic environments always satisfy SBS, that an environmental record persists without a physical carrier, or that an isolated modification of a record changes a later process law.

The most defensible empirical sentence for the ICP paper is:

> Laboratory experiments have demonstrated that interaction-generated information about a quantum system can become redundantly encoded in distinct environmental degrees of freedom and recovered indirectly under controlled conditions.

The paper should **not** turn that sentence into “experiments show information becomes an independent substrate” or “quantum Darwinism proves history governs future law.”

### 1.4 Dynamics are selective, not automatic

Doucet and Deffner classify a broad family of finite-dimensional, at-most-two-body Hamiltonians and show that quantum-Darwinist behavior requires commutation conditions among the system-side interaction operators and a pointer observable. Their result makes an important negative point: redundant classical records do not follow from arbitrary system-environment coupling.

Recent work on noncommuting system and interaction Hamiltonians further shows that objectivity can still arise in explicit models, but the pointer state can depend jointly on \(H_S\), \(H_I\), and sometimes the initial state. Predictability-sieve and SBS criteria coincide cleanly in the commuting regime, not in general. A metrological reformulation based on quantum Fisher information adds a useful operational question—how precisely can a fragment observer estimate the system's initial parameter?—but its exponential rates are demonstrated in a paradigmatic spin-star model, not as a universal law.

For ICP, these results imply that the existence, identity, fidelity, and accessibility of a record are dynamical properties. They cannot be inferred merely from the occurrence of an interaction or from entropy increase.

### 1.5 The factorization objection

All talk of “the system,” “the environment,” and “the fragment” presupposes a subsystem decomposition. Fu proved a sharp non-uniqueness result: the same global state can display redundant imprints of noncommuting observables under different environment decompositions. Uniqueness is recovered only under conditions that make the partitions appropriately comparable.

Adil and collaborators strengthen the concern at the Hamiltonian level. For a fixed Hamiltonian, multiple tensor-product structures can admit robust pointer states and quasiclassical subsystem descriptions; those decompositions need not coincide with familiar spatial locality.

This does not invalidate decoherence or QD in an operationally fixed laboratory. It invalidates an unqualified ontological inference from a redundant record to a unique, decomposition-independent classical world or unique information carrier. In any ICP application, the following must be declared:

- the tensor factorization or observable-algebra split;
- what operations define an accessible fragment;
- which observer/reference-frame resources are available;
- whether the record claim survives comparable refactorizations;
- which spatial, causal, energetic, or control structure privileges the chosen split.

### 1.6 ICP mapping and the missing bridge

A disciplined mapping is:

- **History \(H\):** the interaction history that correlates the source with environmental degrees of freedom.
- **Memory/carrier \(M\):** the conditional physical states of specified fragments, not an abstract bit detached from implementation.
- **Readout class \(\Pi\):** the allowed measurements or operations on those fragments.
- **Future object \(\mathcal{F}\):** the later process tensor, reachable-state set, intervention-response distribution, or transformation family whose dependence on \(M\) is tested.

Existing QD work mainly measures present inference: how much about a source observable can an observer learn from a fragment? ICP asks a stronger causal question: after the record exists, does manipulating the record carrier alter later accessible behavior in a way that cannot be reduced to an uncontrolled difference in the complete present physical state?

The bridge experiment should therefore:

1. Prepare the same controlled reduced state of a target through at least two different histories.
2. Identify and tomographically characterize candidate environment-record carriers.
3. Randomly preserve, erase, swap, scramble, or rewrite the carrier after record formation.
4. Match or explicitly account for energy, conserved charges, ordinary fields, environmental correlations, and control pulses across arms.
5. Apply a common family of later interventions and estimate the conditional process tensor or reachable-state set.
6. Test whether \(P(\text{future outcomes}\mid\text{intervention},M)\) retains predictive/causal dependence on the manipulated record once the complete declared physical state is included.

If standard unitary/open-system dynamics on the augmented state fully explains the effect, the experiment still supports ICP as an organizing language for embodied historical constraints, but not as a new ontological variable or law. A genuinely new-physics claim requires a preregistered residual that standard state-and-dynamics models cannot absorb.

---

## 2. Relational quantum mechanics versus quantum reference frames

### 2.1 They solve different problems

| Question | Relational quantum mechanics | Quantum reference frames |
|---|---|---|
| Primary object | Facts/variable values actualized in interactions, relative to systems. | States, observables, dynamics, and operational equivalence classes described relative to a physical frame. |
| Status | Interpretation/reconstruction of quantum mechanics. | Formal and operational frameworks within quantum mechanics, with several non-equivalent implementations. |
| Core transformation | No single universal “RQM frame-change” map is the defining content. | Typically a unitary, symmetry reduction, gauge fixing, or operational map between perspectives. |
| Invariant content | Quantum probabilities for facts, with cross-perspective claims treated carefully. | Operational probabilities when states and observables are transformed consistently. |
| Memory claim | An interaction produces a relative fact, but RQM does not make every fact a durable physical memory. | A frame supplies relational coordinates/resources; it is not automatically a record of a prior interaction. |
| ICP relevance | Warns against treating properties as absolute and separates facts from state assignments. | Forces explicit frame, observable algebra, symmetry, charge-access, and localization conditions. |
| What it does not establish | A new dynamical history variable, unique inter-observer fact structure, or information-substrate ontology. | Ontological relationalism, persisted history, or information as the substrate of mass/energy/spacetime. |

### 2.2 RQM: relative facts, stable facts, and an active dispute

Rovelli's original RQM proposal treats values of quantum variables as actualized in interactions and meaningful relative to the interacting systems; the quantum state is not an absolute physical condition of a system. Di Biagio and Rovelli later distinguish *relative facts* from *stable facts*. Stability is approximate and relational: interference between alternatives becomes inaccessible to a further system because relevant coherence has dispersed into an environment. It is not generally an exact, observer-free property.

That structure resonates with ICP's interest in interaction history, but the equivalence stops quickly. A fact relative to an interaction is not necessarily an encoded, persistent memory available for future interventions. RQM also does not add a new dynamical term by which accumulated information constrains later possibilities.

The consistency of facts across perspectives remains debated. Pienaar formulated five no-go arguments against a package of RQM commitments involving universality, completeness, unique events, and inter-observer consistency. Di Biagio and Rovelli replied that the objections improperly infer facts relative to one system from a quantum state assigned by another; their response explicitly accepts that RQM abandons some classical cross-perspective intuitions.

For the ICP paper, this exchange should be represented as a live interpretive dispute, not as a resolved empirical theorem favoring relational ontology. RQM currently supplies conceptual discipline, not independent experimental evidence for ICP or IOTA.

### 2.3 QRFs: covariance, operational equivalence, and framework dependence

Giacomini, Castro-Ruiz, and Brukner construct transformations between physical quantum reference frames under which states, observables, dynamics, and measurements are transformed together. Superposition and entanglement can be frame-dependent, while consistently computed observation probabilities agree. Vanrietvelde and collaborators formulate frame choice through a perspective-neutral constrained structure: selecting a frame resembles gauge fixing, and switching frames passes through the neutral description.

These results are important for ICP because they show that state descriptions and even subsystem entanglement are not invariant labels. They do not imply that “information creates reality”; they show how ordinary quantum descriptions change with the physical reference system and constraint treatment.

Recent operational work sharpens the boundaries:

- Carette, Głowacki, and Loveridge define equivalence by indistinguishability under framed/relative observables. Invertible transformations require conditions such as localizability of the destination frame. Different QRF constructions agree operationally only on an appropriate common domain.
- Castro-Ruiz and Oreshkov derive broad relative-subsystem transformations within standard quantum mechanics, reinforcing that a QRF formalism is not automatically a new ontology.
- Doat and Vanrietvelde show that major QRF frameworks are non-equivalent because they impose weak versus strong symmetry constraints. The difference has physical meaning: whether observers can access the global conserved charge. In the weak approach, perspective momenta can be ambiguous and reversible frame transformations may be unavailable.

One July 2026 preprint further distinguishes a laboratory in a spatial superposition from a Wigner-friend-type superposition of measurement outcomes. It is useful as a watchlist item, not as a peer-reviewed cornerstone.

### 2.4 The non-equivalence ICP must preserve

The following implication is invalid:

\[
  \text{RQM says facts are relational}
  \;\Rightarrow\;
  \text{QRF transformations describe those facts}
  \;\Rightarrow\;
  \text{relations are stored information}
  \;\Rightarrow\;
  \text{stored information changes future law}.
\]

Each arrow needs a separate construction or experiment. A reference frame can be a physical quantum system and can limit resolution or available operations, but it need not encode a prior event. A relative fact can result from an interaction, but it need not remain a controllable carrier. Neither formalism selects a unique factorization or guarantees that a proposed ICP variable is invariant.

The productive use of this literature is methodological:

1. Index every proposed record by its carrier, observer algebra, and reference system.
2. State which observable predictions are frame-invariant.
3. Treat changes in entanglement or subsystem labels under a QRF transformation as descriptive unless an operational intervention changes invariant statistics.
4. Specify weak/strong symmetry constraints, accessible charges, and localization assumptions.
5. Demand that an ICP carrier either survive the relevant equivalence transformations or be explicitly described as relational to a declared frame.

---

## 3. Compact boundary: definite and indefinite causal order

### 3.1 The certification ladder

| Level | Meaning | Does not imply |
|---|---|---|
| Definite order | Operations occur as \(A\prec B\) or \(B\prec A\). | That the order is classical in every degree of freedom. |
| Causally separable process | The process is a convex mixture of definite orders. | A coherent superposition of orders. |
| Causally nonseparable process | The process cannot be decomposed as such a mixture; often detected with a causal witness and trusted operation model. | Violation of a causal inequality or device-independent certification. |
| Causal-inequality violation | Observed correlations violate a bound satisfied by a stated class of definite-order causal models, under free-choice/closed-lab/locality assumptions. | A superposition of localized spacetime causal structures. |
| Indefinite spacetime causal structure | Causal relations among localized spacetime events or geometries are in quantum superposition/indefinite. | Emergence of spacetime or causality from information. |

Oreshkov, Costa, and Brukner introduced process matrices that retain local quantum mechanics while dropping a globally fixed causal order; the framework contains theoretical correlations that violate a causal inequality. Chiribella and collaborators introduced the quantum switch as coherent control of the sequence in which operations act on a target.

Photonic quantum-switch experiments have certified causal nonseparability with causal witnesses. Rubino and collaborators reported an experimental witness violation at roughly seven standard deviations; Goswami and collaborators reported a stronger witness and an implementation in which the operations were not assigned distinguishable fixed spatial or temporal positions in the relevant description. These are meaningful process-level results, but the certification depends on a trusted description of devices and allowed operations.

### 3.2 Why “indefinite order” is not one claim

Paunković and Vojinović show that circuit causal order and spacetime-event causal order must be distinguished. Standard photonic switches can be embedded in a classical spacetime with a definite event structure, whereas a proposed gravitational switch involves superposed gravitational configurations. Ormrod, Vanrietvelde, and Barrett show that sectorial constraints matter: a photonic switch may have a cyclic coarse-grained causal description while retaining an acyclic fine-grained structure. They therefore characterize current experiments as realizing only a weaker form of indefinite order.

Vilasini and Renner make the information-theoretic/spacetime distinction explicit by embedding cyclic information-processing structures in acyclic spacetime and deriving consistency constraints. This is the correct boundary for ICP: an information-processing graph need not be the causal structure of spacetime.

Purves and Short proved that a broad standard class of quantum protocols—in which each party interacts once under their stated assumptions—cannot violate a causal inequality because the correlations admit a classical causal simulation. This is not a theorem that *all conceivable quantum experiments* can never violate such an inequality. Later proposals alter operational structure and add assumptions that make a stronger witness possible.

### 3.3 The 2026 causal-order experiment

Guo and collaborators report a photonic Bell-like test of causal order. The order of two optical processes on a target is controlled by one photon of a polarization-entangled pair; kilometer-scale fiber is used to implement the required separation structure. The reported value is \(1.807\pm0.010\) against a bound of \(1.75\), a 5.7-standard-deviation violation.

The authors do not claim a loophole-free device-independent demonstration. The inference depends on free-intervention and relativistic separation assumptions, and locality, fair-sampling, free-choice, and device/setup-knowledge loopholes remain. The defensible statement is:

> A 2026 proof-of-principle photonic experiment violated a Bell-like causal-order inequality under stated operational and relativistic assumptions, while leaving significant loopholes open.

It should not be summarized as “definite causality has been experimentally disproved.”

### 3.4 ICP relevance and stopping rule

The quantum switch is useful to ICP because an identifiable physical control determines a coherent family of future operation sequences. It demonstrates that the space of available transformations can itself be conditioned by a quantum degree of freedom. But that control is usually prepared for the protocol; it is not automatically a record accumulated from a prior interaction, and its standard quantum state already carries the predictive content.

Thus:

\[
\text{controlled future-order family}
\not\Rightarrow
\text{history-generated memory}
\not\Rightarrow
\text{new constraint law}
\not\Rightarrow
\text{emergent spacetime}.
\]

The causal-order literature is closed at this boundary for the present synthesis. Additional protocol advantages, higher-order maps, or quantum-gravity proposals should enter only if ICP specifies a concrete claim about causal-order control that they can discriminate.

---

## 4. Integrated viability assessment

### 4.1 What survives adversarial scrutiny

The strongest common architecture across the three literatures is operational and physical:

1. Interactions generate correlations.
2. Some correlations become embodied in distinguishable states of secondary systems.
3. The information available from those states depends on the subsystem split, observable algebra, reference frame, and allowed operations.
4. A physical degree of freedom can condition which later transformations or operational orders are available.

This is a defensible scientific base for studying **embodied, interaction-generated constraints on counterfactual futures**. It makes the ICP program worth pursuing.

### 4.2 What does not survive as an established conclusion

The literature does not license any of the following without new work:

- information persists independently of all physical carriers;
- redundancy chooses a unique system/environment decomposition;
- observer agreement follows from decoherence alone;
- a relative fact in RQM is the same thing as a stored record;
- QRF covariance demonstrates ontological information primacy;
- causal nonseparability means spacetime events lack definite order;
- a stored record changes fundamental law rather than initial/boundary conditions within ordinary dynamics;
- mass and energy emerge from an information lattice.

### 4.3 Honest verdict

**Viability: promising research architecture, not established physical principle.**

The record-formation premise has direct theoretical and experimental support. The “constraint on counterfactual futures” premise is scientifically coherent if expressed as an intervention-indexed claim about reachable states or processes. Its novelty is presently underdetermined: standard quantum mechanics already predicts that the physical state of a memory-bearing environment can affect future dynamics. ICP becomes more than a useful redescription only if it either:

- derives a nontrivial, cross-domain quantitative law from a compact constraint variable; or
- predicts an intervention outcome not captured by a complete standard description of the joint physical state and dynamics.

This verdict supports proceeding with the paper, provided the paper presents ICP as a staged research program and uses the evidence ladder explicitly.

---

## 5. Proposed claim–evidence rows for the master matrix

These rows are written so they can be imported or split into one-source rows. “ICP use” is deliberately distinct from the cited result.

| ID | Level | Proposed claim | Primary evidence and locator | Limitation / rival explanation | ICP use |
|---|---|---|---|---|---|
| QRF-C01 | field_result | Under appropriate system–environment interactions, information about a preferred system observable can be selectively proliferated into multiple environmental fragments. | Ollivier, Poulin & Zurek (2004), abstract and environment-as-witness construction; DOI [10.1103/PhysRevLett.93.220401](https://doi.org/10.1103/PhysRevLett.93.220401). | Model-dependent interaction and declared partition; no proof of carrier-independent information or future-law change. | Positive mechanism for source-to-secondary-carrier record formation. |
| QRF-C02 | field_result | For a finite-dimensional input channel distributed over many outputs, most small fragment channels are approximately measure-and-prepare channels for one common POVM. | Brandão, Piani & Horodecki (2015), main theorem; DOI [10.1038/ncomms8908](https://doi.org/10.1038/ncomms8908). | Common observable does not guarantee distinguishable outcome states, perfect redundancy, or unique partition. | Supports generic classicalization of fragment-accessible observable information, not generic objective outcomes. |
| QRF-C03 | field_result | A quantum-mutual-information plateau is not sufficient for spectrum-broadcast objectivity, and redundancy need not equal operational consensus. | Le & Olaya-Castro (2018), comparison examples, DOI [10.1103/PhysRevA.98.032103](https://doi.org/10.1103/PhysRevA.98.032103); Chisholm, Innocenti & Palma (2023), nonlocal-encoding analysis, DOI [10.22331/q-2023-08-03-1074](https://doi.org/10.22331/q-2023-08-03-1074). | Different measures answer different operational questions; terminology varies. | Prevents treating correlation or agreement as independent physical copies. |
| QRF-C04 | field_result | Controlled experiments have observed redundant imprints of a system observable in distinct environmental degrees of freedom. | Unden et al. (2019), NV electron plus \(^{13}\mathrm C\) spin environment, abstract/results; DOI [10.1103/PhysRevLett.123.140402](https://doi.org/10.1103/PhysRevLett.123.140402). | Few-spin, highly controlled platform; authors claim incipient, not universal, objectivity. | Direct evidence for physically embodied secondary records. |
| QRF-C05 | field_result | Quantum-Darwinist record formation requires dynamical structure and is not implied by arbitrary two-body coupling. | Doucet & Deffner (2024), classification theorem and examples; DOI [10.1103/PhysRevX.14.041064](https://doi.org/10.1103/PhysRevX.14.041064). | Finite-dimensional environment and at-most-two-body Hamiltonian class; criterion tied to their QD definition. | Motivates specifying carrier-formation conditions rather than assuming all interactions make memories. |
| QRF-C06 | field_result | The observable appearing redundantly recorded can depend on the environment partition; the same global state can support redundant imprints of noncommuting observables under different decompositions. | Fu (2021), Eqs. (1)–(2), comparable-partition condition and uniqueness analysis; DOI [10.1103/PhysRevA.103.042210](https://doi.org/10.1103/PhysRevA.103.042210). | Operationally fixed laboratory partitions may be privileged; non-comparable decompositions need not be simultaneously accessible. | Requires ICP records to be indexed by decomposition/algebra and tested for appropriate invariance. |
| QRF-C07 | field_result | A fixed Hamiltonian can admit multiple tensor-product structures with robust pointer states, not necessarily aligned with familiar classical locality. | Adil et al. (2026), abstract and derived Hamiltonian forms; DOI [10.1103/vj4x-96fk](https://doi.org/10.1103/vj4x-96fk). | Mathematical factorizations are not automatically equally operationally realizable. | Strongest current objection to unqualified unique-carrier or unique-classical-world claims. |
| QRF-C08 | field_result | In RQM, facts are relative to interactions and “stable facts” are approximate and relational; consistency across perspectives remains interpretively contested. | Di Biagio & Rovelli (2021), stable-facts analysis, DOI [10.1007/s10701-021-00429-w](https://doi.org/10.1007/s10701-021-00429-w); Pienaar (2021), five no-go arguments, DOI [10.1007/s10701-021-00500-6](https://doi.org/10.1007/s10701-021-00500-6); reply DOI [10.1007/s10701-022-00579-5](https://doi.org/10.1007/s10701-022-00579-5). | Interpretive dispute; no independent experimental discriminator or added dynamics. | Supplies relational discipline, not evidence that facts are stored ICP constraints. |
| QRF-C09 | field_result | Under consistent QRF transformations, superposition and entanglement can be frame-relative while operational probabilities remain invariant. | Giacomini, Castro-Ruiz & Brukner (2019), transformation of states/dynamics/measurements; DOI [10.1038/s41467-018-08155-0](https://doi.org/10.1038/s41467-018-08155-0). | Constructed within quantum theory and stated frame model; frame relativity is not ontological information primacy. | ICP claims should identify frame-dependent descriptions and frame-invariant predictions. |
| QRF-C10 | field_result | QRF frameworks can be operationally non-equivalent; invertibility and even the content of a perspective depend on localization, symmetry constraints, and charge accessibility. | Carette, Głowacki & Loveridge (2025), operational equivalence/localizability, DOI [10.22331/q-2025-03-27-1680](https://doi.org/10.22331/q-2025-03-27-1680); Doat & Vanrietvelde (2026), weak/strong constraints and charge access, DOI [10.22331/q-2026-06-08-2126](https://doi.org/10.22331/q-2026-06-08-2126). | Conclusions are framework- and symmetry-domain-specific. | Blocks references to “the QRF transformation” without declaring operational resources. |
| QRF-C11 | field_result | Causal nonseparability of an information-processing description is not sufficient to establish indefinite order among localized spacetime events. | Paunković & Vojinović (2020), circuit/spacetime embeddings, DOI [10.22331/q-2020-05-28-275](https://doi.org/10.22331/q-2020-05-28-275); Ormrod, Vanrietvelde & Barrett (2023), fine/coarse-grained causal structures, DOI [10.22331/q-2023-06-01-1028](https://doi.org/10.22331/q-2023-06-01-1028). | Event ontology and allowed operation sector matter; gravitational-switch proposals are separate. | Keeps operational future-order control distinct from emergent spacetime causality. |
| QRF-C12 | field_result | A 2026 photonic experiment violated a Bell-like causal-order inequality by 5.7 standard deviations under stated assumptions, with acknowledged loopholes. | Guo et al. (2026), reported \(1.807\pm0.010\) versus 1.75 bound and limitations discussion; DOI [10.1126/sciadv.aee2912](https://doi.org/10.1126/sciadv.aee2912). | Not loophole-free or fully device-independent; locality, fair-sampling, free-choice, and setup assumptions remain. | Shows stronger operational certification is becoming possible; does not establish indefinite spacetime or ICP. |

Two synthesis rows should accompany those field rows in prose or in a separate synthesis matrix:

- **QRF-S01 (synthesis_inference):** QD experiments support persistence of information *away from the original bearer* but only in other physical carriers. They do not support persistence independent of physical realization.
- **QRF-S02 (icp_hypothesis):** after matching the declared present state and resources, a targeted intervention on a history-generated record carrier changes the later reachable process family. This is the missing discriminating test, not a result of any source above.

---

## 6. Primary-source register

### Decoherence, objectivity, and records

1. W. H. Zurek, “Decoherence, einselection, and the quantum origins of the classical,” *Reviews of Modern Physics* **75**, 715 (2003). DOI: [10.1103/RevModPhys.75.715](https://doi.org/10.1103/RevModPhys.75.715). Foundational orientation; review status means later primary theorems/experiments carry the evidentiary load.
2. H. Ollivier, D. Poulin, and W. H. Zurek, “Objective Properties from Subjective Quantum States: Environment as a Witness,” *Physical Review Letters* **93**, 220401 (2004). DOI: [10.1103/PhysRevLett.93.220401](https://doi.org/10.1103/PhysRevLett.93.220401).
3. H. Ollivier, D. Poulin, and W. H. Zurek, “Environment as a witness: Selective proliferation of information and emergence of objectivity in a quantum universe,” *Physical Review A* **72**, 042113 (2005). DOI: [10.1103/PhysRevA.72.042113](https://doi.org/10.1103/PhysRevA.72.042113).
4. F. G. S. L. Brandão, M. Piani, and P. Horodecki, “Generic emergence of classical features in quantum Darwinism,” *Nature Communications* **6**, 7908 (2015). DOI: [10.1038/ncomms8908](https://doi.org/10.1038/ncomms8908).
5. R. Horodecki, J. K. Korbicz, and P. Horodecki, “Quantum origins of objectivity,” *Physical Review A* **91**, 032122 (2015). DOI: [10.1103/PhysRevA.91.032122](https://doi.org/10.1103/PhysRevA.91.032122).
6. T. P. Le and A. Olaya-Castro, “Objectivity (or lack thereof): Comparison between predictions of quantum Darwinism and spectrum broadcast structure,” *Physical Review A* **98**, 032103 (2018). DOI: [10.1103/PhysRevA.98.032103](https://doi.org/10.1103/PhysRevA.98.032103).
7. T. P. Le and A. Olaya-Castro, “Strong Quantum Darwinism and Strong Independence are Equivalent to Spectrum Broadcast Structure,” *Physical Review Letters* **122**, 010403 (2019). DOI: [10.1103/PhysRevLett.122.010403](https://doi.org/10.1103/PhysRevLett.122.010403).
8. A. Feller et al., “Comment on ‘Strong Quantum Darwinism and Strong Independence are Equivalent to Spectrum Broadcast Structure,’” *Physical Review Letters* **126**, 188901 (2021). DOI: [10.1103/PhysRevLett.126.188901](https://doi.org/10.1103/PhysRevLett.126.188901); author reply: [10.1103/PhysRevLett.126.188902](https://doi.org/10.1103/PhysRevLett.126.188902).
9. D. A. Chisholm, L. Innocenti, and G. M. Palma, “The meaning of redundancy and consensus in quantum objectivity,” *Quantum* **7**, 1074 (2023). DOI: [10.22331/q-2023-08-03-1074](https://doi.org/10.22331/q-2023-08-03-1074).
10. M. A. Ciampini et al., “Experimental signature of quantum Darwinism in photonic cluster states,” *Physical Review A* **98**, 020101(R) (2018). DOI: [10.1103/PhysRevA.98.020101](https://doi.org/10.1103/PhysRevA.98.020101).
11. M.-C. Chen et al., “Emergence of classical objectivity of quantum Darwinism in a photonic quantum simulator,” *Science Bulletin* **64**, 580–585 (2019). DOI: [10.1016/j.scib.2019.03.032](https://doi.org/10.1016/j.scib.2019.03.032).
12. T. Unden et al., “Revealing the Emergence of Classicality Using Nitrogen-Vacancy Centers,” *Physical Review Letters* **123**, 140402 (2019). DOI: [10.1103/PhysRevLett.123.140402](https://doi.org/10.1103/PhysRevLett.123.140402).
13. Emery Doucet and Sebastian Deffner, “Classifying Two-Body Hamiltonians for Quantum Darwinism,” *Physical Review X* **14**, 041064 (2024). DOI: [10.1103/PhysRevX.14.041064](https://doi.org/10.1103/PhysRevX.14.041064).
14. Anthony Kiely et al., “Metrological approach to the emergence of classical objectivity,” *Physical Review A* **113**, 022403 (2026). DOI: [10.1103/hn78-7xx3](https://doi.org/10.1103/hn78-7xx3).
15. Diana A. Chisholm, G. Massimo Palma, and Luca Innocenti, “Emergence of quantum Darwinism and pointer states for noncommuting evolutions,” *APS Open Science* **1**, 000024 (2026). DOI: [10.1103/75jr-ltct](https://doi.org/10.1103/75jr-ltct).
16. Hui-Feng Fu, “Uniqueness of the observable leaving redundant imprints in the environment in the context of quantum Darwinism,” *Physical Review A* **103**, 042210 (2021). DOI: [10.1103/PhysRevA.103.042210](https://doi.org/10.1103/PhysRevA.103.042210).
17. Arsalan Adil et al., “Search for classical subsystems in quantum worlds,” *Physical Review D* **113**, 103535 (2026). DOI: [10.1103/vj4x-96fk](https://doi.org/10.1103/vj4x-96fk).

### RQM and quantum reference frames

18. Carlo Rovelli, “Relational Quantum Mechanics,” *International Journal of Theoretical Physics* **35**, 1637–1678 (1996). DOI: [10.1007/BF02302261](https://doi.org/10.1007/BF02302261).
19. Andrea Di Biagio and Carlo Rovelli, “Stable Facts, Relative Facts,” *Foundations of Physics* **51**, 30 (2021). DOI: [10.1007/s10701-021-00429-w](https://doi.org/10.1007/s10701-021-00429-w).
20. Jacques Pienaar, “A Quintet of Quandaries: Five No-Go Theorems for Relational Quantum Mechanics,” *Foundations of Physics* **51**, 97 (2021). DOI: [10.1007/s10701-021-00500-6](https://doi.org/10.1007/s10701-021-00500-6).
21. Andrea Di Biagio and Carlo Rovelli, “Relational Quantum Mechanics is About Facts, Not States: A Reply to Pienaar and Brukner,” *Foundations of Physics* **52**, 62 (2022). DOI: [10.1007/s10701-022-00579-5](https://doi.org/10.1007/s10701-022-00579-5).
22. Flaminia Giacomini, Esteban Castro-Ruiz, and Časlav Brukner, “Quantum mechanics and the covariance of physical laws in quantum reference frames,” *Nature Communications* **10**, 494 (2019). DOI: [10.1038/s41467-018-08155-0](https://doi.org/10.1038/s41467-018-08155-0).
23. Augustin Vanrietvelde et al., “A change of perspective: switching quantum reference frames via a perspective-neutral framework,” *Quantum* **4**, 225 (2020). DOI: [10.22331/q-2020-01-27-225](https://doi.org/10.22331/q-2020-01-27-225).
24. Titouan Carette, Michał Głowacki, and Leon Loveridge, “Operational Quantum Reference Frame Transformations,” *Quantum* **9**, 1680 (2025). DOI: [10.22331/q-2025-03-27-1680](https://doi.org/10.22331/q-2025-03-27-1680).
25. Esteban Castro-Ruiz and Ognyan Oreshkov, “Relative subsystems and quantum reference frame transformations,” *Communications Physics* **8**, 187 (2025). DOI: [10.1038/s42005-025-02036-x](https://doi.org/10.1038/s42005-025-02036-x).
26. Guilhem Doat and Augustin Vanrietvelde, “What can we do in a symmetry-constrained perspective? The importance of the total charge's status in quantum reference frame frameworks,” *Quantum* **10**, 2126 (2026). DOI: [10.22331/q-2026-06-08-2126](https://doi.org/10.22331/q-2026-06-08-2126).
27. Augustin Vanrietvelde, “Specifying the operational meaning of quantum reference frames,” arXiv:2607.03417 (2026), DOI: [10.48550/arXiv.2607.03417](https://doi.org/10.48550/arXiv.2607.03417). **Unreviewed preprint; watchlist only.**

### Causal order

28. Ognyan Oreshkov, Fabio Costa, and Časlav Brukner, “Quantum correlations with no causal order,” *Nature Communications* **3**, 1092 (2012). DOI: [10.1038/ncomms2076](https://doi.org/10.1038/ncomms2076).
29. Giulio Chiribella et al., “Quantum computations without definite causal structure,” *Physical Review A* **88**, 022318 (2013). DOI: [10.1103/PhysRevA.88.022318](https://doi.org/10.1103/PhysRevA.88.022318).
30. Giulia Rubino et al., “Experimental verification of an indefinite causal order,” *Science Advances* **3**, e1602589 (2017). DOI: [10.1126/sciadv.1602589](https://doi.org/10.1126/sciadv.1602589).
31. K. Goswami et al., “Indefinite Causal Order in a Quantum Switch,” *Physical Review Letters* **121**, 090503 (2018). DOI: [10.1103/PhysRevLett.121.090503](https://doi.org/10.1103/PhysRevLett.121.090503).
32. Nikola Paunković and Marko Vojinović, “Causal orders, quantum circuits and spacetime: distinguishing between definite and superposed causal orders,” *Quantum* **4**, 275 (2020). DOI: [10.22331/q-2020-05-28-275](https://doi.org/10.22331/q-2020-05-28-275).
33. Tom Purves and Anthony J. Short, “Quantum Theory Cannot Violate a Causal Inequality,” *Physical Review Letters* **127**, 110402 (2021). DOI: [10.1103/PhysRevLett.127.110402](https://doi.org/10.1103/PhysRevLett.127.110402).
34. David Ormrod, Augustin Vanrietvelde, and Jonathan Barrett, “Causal structure in the presence of sectorial constraints, with application to the quantum switch,” *Quantum* **7**, 1028 (2023). DOI: [10.22331/q-2023-06-01-1028](https://doi.org/10.22331/q-2023-06-01-1028).
35. V. Vilasini and Renato Renner, “Embedding cyclic information-theoretic structures in acyclic space-times: no-go results for process matrices,” *Physical Review A* **110**, 022227 (2024), with correction posted 2026-07-15. DOI: [10.1103/PhysRevA.110.022227](https://doi.org/10.1103/PhysRevA.110.022227).
36. Yu Guo et al., “Experimental violation of a Bell-like inequality for causal order,” *Science Advances* **12** (2026), article eaee2912. DOI: [10.1126/sciadv.aee2912](https://doi.org/10.1126/sciadv.aee2912).

---

## 7. Closure audit and remaining bounded gaps

Searches were run across three strata: (1) QD mechanism, objectivity definitions, experiments, Hamiltonian conditions, and factorization critiques; (2) RQM primary statement, no-go critique/reply, QRF transformations, operational equivalence, and framework non-equivalence; and (3) process matrices, quantum switches, causal witnesses/inequalities, and information-theoretic versus spacetime causality. Primary journal pages, journal-hosted full texts, and official repositories were preferred. The 2026 cutoff was checked specifically for new QD classifications/measures, QRF framework comparisons, factorization results, and the causal-order experiment.

Conceptual saturation was reached for the present paper: newer QD work refines the dynamical and measurement conditions but does not close the future-constraint bridge; newer QRF work strengthens the need to state operational domains rather than producing a unique framework; and newer causal-order work strengthens certification while preserving the distinction from spacetime causal structure.

The following are intentionally left as later, question-triggered work rather than literature gaps blocking the synthesis:

- full quantum process-tensor/non-Markovian-memory review for designing the decisive experiment;
- algebraic-QFT subsystem and gauge-dressing issues beyond the finite-dimensional factorization warning;
- quantum-gravity reference frames and gravitational switches beyond the causal-order boundary;
- device-independent causal-order protocols beyond the 2026 proof of principle;
- a quantitative measure converting record intervention into a change in a counterfactual reachable set.

None of those prevents an honest synthesis paper now. They define the next experimental and formal work packages if ICP survives the larger cross-domain viability review.
