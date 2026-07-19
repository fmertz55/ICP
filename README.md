# ICP literature review and synthesis

## Purpose

This project critically evaluates a candidate Information-Constraint Principle
(ICP): physically embodied organization, potentially including records of prior
interactions, can restrict or reweight the future states and transformations
available to a system.

The grounding target is ICP in general. The supplied Dirac operational-role
manuscript is one possible downstream application or test case; it does not
define the review's inclusion criteria, vocabulary, or evidentiary direction.

The project is designed to evaluate that proposition, not to validate it. A
scientifically useful result may support, narrow, reformulate, render redundant,
or reject ICP.

## Current status

Pilot Batch 01 is complete for the formal core: constructor theory, quantum
process memory, computational mechanics, macrostates/path ensembles, and causal
semantics. It registers 19 sources (18 included peer-reviewed sources and one
current background preprint), 31 source-claim relations, individual extraction
notes, and a cross-domain comparison.

Pilot Batch 02 is complete for Zipf mechanism discrimination. It adds 19
peer-reviewed sources spanning preferential growth, random typing, least
effort, latent mixtures, criticality, maximum entropy, sample-space reduction,
dynamical coherence, finite-sample inference, and Heaps/type-token dynamics.
Its principal finding is deliberately negative but productive: a Zipf marginal
does not identify a mechanism and is not evidence of memory, embodiment, or ICP.
The ICP-relevant object is the intervention-sensitive law of the next event,
novelty, or reachable successor set after histories have been matched on their
present marginal counts.

Start with `synthesis/pilot_batch_01_formal_core.md`, then read
`synthesis/pilot_batch_02_zipf_mechanism_discrimination.md`. Project-generated
PSA evidence is quarantined from the literature synthesis under
`project_evidence/`; its first audit discovered an adaptive-routing censoring
boundary that invalidates a naive fit to the stored mixed-resolution voxel
counts.

## Core review question

Across the selected scientific fields, under what operational definitions and
formal or empirical results does present organization or interaction history
differentiate a system's accessible future transformations or state
distributions? What additional testable content, if any, would ICP contribute
beyond established dynamics?

The common comparison schema is a family of future laws under declared
interventions:

`history H_t -> physically embodied record M_t -> {P^pi(F[t:t+tau] | M_t) : pi in Pi}`

Hard reachability is the support of a specified future law; probabilistic
constraint is its weighting over that support. A predictive distribution,
`P(F | H)`, is not automatically counterfactual. Counterfactual comparison asks
what the same modeled system would do under a different intervention or policy
and therefore requires causal assumptions beyond ordinary conditioning.

For each field, the review asks what `H`, `M`, `F`, and the admissible
intervention family `Pi` mean, where `M` is physically represented, what
comparison establishes a constraint, and whether the apparent history
dependence disappears when the system state is enlarged.

## Scientific stance

- Treat ICP as a working hypothesis, not an established law or ontology.
- Keep three claim levels separate: **established field result**,
  **cross-field synthesis inference**, and **ICP hypothesis**.
- Preserve each field's native definitions before translating them into ICP
  language.
- Distinguish logical possibility, dynamical accessibility, probabilistic
  weighting, predictive equivalence, and organizational maintenance.
- Record evidence that supports, qualifies, challenges, is neutral toward, or
  is only analogous to ICP.
- Pair every proposed similarity with its strongest disanalogy or rival account.
- Require exact page, section, theorem, equation, figure, or dataset locators for
  consequential claims.
- Use primary sources for technical claims; use reviews mainly for orientation
  and citation discovery.
- Do not use the supplied manuscript or IOTA simulation results as evidence in
  this literature-only synthesis.

## Project structure

```text
ICP/
├── README.md
├── docs/          # Supplied project context; not literature evidence
├── protocol/      # Review method and auditable amendments
├── searches/      # Exact queries and search-run log
├── library/       # Source registry, bibliography, and local full texts
├── notes/         # One structured note per included source
├── analysis/      # Claim/evidence links, rivals, and falsification criteria
├── synthesis/     # Cross-domain comparison and evolving synthesis
├── project_evidence/ # Internal data audits and preregistrations; never literature
└── manuscript/    # Provisional outline, drafts, tables, and figures
```

The proposed research areas are provisional search strata, not pre-established
"pillars." Sources are stored once and tagged across domains rather than placed
in theory-specific folders. This prevents the initial taxonomy from hardening
into a conclusion.

Initial search strata include:

1. possible/impossible transformations, resource theories, and reachability;
2. decoherence, environmental records, and quantum Darwinism;
3. non-Markovian dynamics, process tensors, and physical memory;
4. computational mechanics, causal states, predictive structure, and
   intervention-aware state equivalence;
5. statistical mechanics, macrostates, path ensembles, large deviations, and
   scaling laws, with Zipf as a discriminating case rather than presumed
   evidence;
6. relational quantum approaches, physical reference frames, and
   observable-algebra dependence;
7. biological organization, constraint closure, autocatalysis, and heredity;
8. cross-cutting information thermodynamics, causal intervention, control, and
   scale or observer dependence;
9. the quantum-gravitational frontier, including black-hole information,
   holographic encoding, generalized entropy, and recoverability, treated as a
   stress test rather than foundational confirmation;
10. critical literature, no-go results, reductive explanations, and null models.

## Working method

1. Freeze or amend the protocol before each search phase.
2. Log every database query exactly in `searches/search_log.csv`.
3. Register candidates and exclusions in `library/source_index.csv`.
4. Assign stable IDs (`S001` sources, `C001` claims, `R001` rivals, `F001`
   falsification criteria).
5. Create one source note from `notes/source_note_template.md`.
6. Enter one row per source-claim relationship in
   `analysis/claim_evidence_matrix.csv`.
7. Compare fields by formal object and causal structure in
   `synthesis/cross_domain_map.csv`, not merely by shared vocabulary.
8. Update the synthesis and manuscript only after contradictory evidence and
   alternative explanations have been assessed.

The scoped expansion for statistics, Zipf, and black-hole information is in
`synthesis/research_agenda_statistics_zipf_black_holes.md`. The completed Zipf
batch includes an adversarial mechanism matrix in
`analysis/zipf_mechanism_matrix.csv` and a preregistration-ready PSA design in
`project_evidence/psa_zipf_preregistration.md`.

## Novelty gate

Before ICP is called a principle, the project must identify at least one
well-defined quantity, invariant, prediction, prohibition, explanatory
compression, or experimental discriminator that is not already supplied by a
fully specified standard dynamical model. If it cannot, the honest product is a
constraint-based synthesis or research heuristic rather than a new physical
principle.
