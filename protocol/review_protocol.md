# ICP structured critical-synthesis protocol

- Protocol version: 0.8
- Date: 2026-07-21
- Status: pilot protocol
- Review type: structured critical-scoping review with integrative synthesis

This project should not be described as a systematic review unless later work
performs an appropriately exhaustive search, reproducible screening, and an
independent audit or duplicate-screening process. Protocol changes are recorded
in `amendments.csv` rather than silently incorporated.

## 1. Objective

Evaluate whether separate scientific programs contain formal or empirical
results that instantiate a shared structure over a declared family of
interventions or policies:

`history H_t -> embodied record M_t -> {P^pi(F[t:t+tau] | M_t) : pi in Pi}`

For a specified `pi`, hard accessibility is represented by the support of the
future law and soft constraint by its probability weighting. Predictive,
interventional, and counterfactual claims must be labeled separately. A family
of conditional distributions is not a counterfactual model unless the causal
assumptions linking alternative interventions are supplied.

The review tests whether that structure is genuinely shared, merely analogous,
or already exhausted by ordinary dynamics and state specification.

## 2. Research questions

1. What does each field operationally mean by information, constraint, state,
   history, possibility, accessibility, and future?
2. What physical carrier or organization retains the relevant distinction, at
   what scale and relative to what system-environment partition?
3. What formal theorem, model, experiment, simulation, or intervention connects
   that distinction to a future reachable set or conditional distribution?
4. Is the source making a predictive, interventional, or counterfactual claim,
   and what assumptions identify it?
5. Are cross-field mappings verbal, structural, formally isomorphic, or
   derivational? Where do they fail?
6. Which boundary conditions, coarse-grainings, observational choices, or
   omitted variables generate or remove the claimed history dependence?
7. What does ICP predict, prohibit, compress, or explain beyond a fully specified
   standard dynamical account?
8. What evidence would narrow, falsify, or make the proposal redundant?
9. Does a claimed novelty represent a newly visited member of a fixed space,
   a change in accessibility, a new registered type or relation, or a change in
   the generative state space itself?

## 3. Claim levels

Every material claim receives exactly one level:

- `field_result`: demonstrated or argued within the source's own framework;
- `synthesis_inference`: a cross-source or cross-field interpretation made here;
- `icp_hypothesis`: content added by the proposed ICP framework.

Language such as "shows" or "establishes" is reserved for results justified at
the first level. Cross-domain recurrence does not by itself establish a common
mechanism or an ontological principle.

## 4. Eligibility

### Include

- Primary formal, theoretical, experimental, or computational work defining a
  physical state, structure, memory, correlation, constraint, or organization
  and relating it to transformations or conditional future behavior.
- Substantive critical work, counterexamples, no-go results, and rival accounts.
- High-quality reviews used for orientation, terminology, and citation chaining.
- Work that clarifies when apparent memory or constraint is dependent on
  partition, coarse-graining, intervention scheme, or state representation.

### Exclude or mark background-only

- Metaphorical uses of "information" or "constraint" without operational or
  formal content.
- Broad claims that reality "is information" without a physical mechanism or
  discriminating implication.
- Shannon-information calculations lacking a relevant physical or predictive
  connection.
- Generic biological complexity used as evidence for fundamental physics.
- Tertiary repetition when the primary result is available.
- The supplied project manuscripts and IOTA results as supporting literature.
  They may be analyzed in a separately labeled project-evidence stratum, but
  never counted as independent validation of their own premises.

No date restriction is imposed during the pilot. Language and full-text access
limitations must be recorded, not converted into claims of absence.

## 5. Search strategy

Search each field first in its native vocabulary. Do not require ICP wording for
inclusion. Each search run must record the platform, exact query, filters,
returned result count, screening count, inclusion count, date, and protocol
version in `searches/search_log.csv`.

For each provisional search stratum, seek at minimum:

- a foundational source;
- a current review or authoritative overview;
- a strong primary formal or empirical result;
- a substantive critique, limitation, null result, or competing explanation.

Use backward and forward citation chaining. Run adversarial searches explicitly,
including terms such as critique, limitation, counterexample, no-go, Markovian
embedding, state augmentation, observer dependence, coarse-graining, and
alternative explanation. Save long or reusable queries in `searches/queries/`.

Statistics is treated as shared formal language across the seven original
literature programs, not as an additional confirming pillar. Zipf's law is a
mechanism-discrimination case: a rank-frequency marginal is insufficient to
infer inherited constraint. Black-hole information is a frontier stress test;
controlled holographic or gravitational results must be separated from claims
about evaporating astrophysical black holes.

Entropy is treated as a cross-cutting stress test, not as a synonym for
constraint. Every entropy claim must declare the underlying state or path
space, measure or reference state, coarse-graining or observable algebra,
allowed operation family, task, horizon, and error tolerance. Searches must
separate support restriction, probability reweighting, accessibility orders,
entropy rate, predictive memory, entropy production, rare-event conditioning,
one-shot tasks, generalized entropies, and algebraic entropy.

The adjacent possible is treated as a question-triggered prior-art and
support-creation audit, not as a new confirming pillar. Searches must separate
Kauffman's one-step molecular definition; enablement and unprestatability
claims; urn triggering; network exploration; combinatorial TAP models;
higher-order novelty; scaffolding; and resource-constrained empirical tests.
Heaps, Zipf, Taylor, clustering, or hockey-stick scaling alone cannot identify
an adjacent-possible mechanism or ICP. Each material claim must declare the
actualized repertoire, novelty/type classifier, meaning of one step, generative
rule, policy, horizon, resources, and whether possibilities are created,
enabled, discovered, or merely relabeled.

## 6. Screening and source registration

Screen title/abstract first, then full text where warranted. Record all candidate
sources in `library/source_index.csv` with one of:

- `candidate`
- `included`
- `background`
- `excluded`

Every exclusion receives a short reason. Preserve duplicate and inaccessible
records as statuses rather than deleting them. In a one-reviewer pilot, perform
a deliberate second pass over all cornerstone, ambiguous, and contrary sources.
If collaborators join, independently audit at least a sample and all pivotal
sources.

## 7. Extraction

Use the note template without replacing a source's terminology with ICP terms.
During a bounded closure batch, a structured adversarial dossier may serve as
the note container for several sources only when each source retains a stable
source-registry row, source-level claim--evidence rows, a primary locator,
verification status, limitations, and a unique bibliography key. The dossier
must preserve the source's native claim before giving the ICP mapping. This
consolidation changes document packaging, not the evidentiary requirements.
Extract:

- system, model, scale, and system-environment partition;
- admissible intervention or policy family and observable algebra;
- author-defined information, constraint, state/history, and future object;
- for adjacent-possible claims: actual set, adjacent frontier, type/role map,
  step or horizon, novelty-versus-innovation status, generative rule, resource
  constraint, and enabled/lost/retained identities;
- for entropy claims: functional, state/path space, measure or reference,
  partition/algebra, allowed operations, task, horizon, and tolerance;
- method or formalism and the exact result;
- assumptions, boundary conditions, interventions, and comparison case;
- empirical status and maturity;
- alternative interpretation;
- direction and directness of the ICP relationship;
- exact page, section, theorem, equation, figure, or data locator.

Each row in `analysis/claim_evidence_matrix.csv` represents one source-claim
relationship. A paper may therefore generate multiple rows with different
directions or levels.

## 8. Appraisal dimensions

Do not collapse quality into a single score. Record separately:

- evidence type: formal result, experiment, simulation, review, or conceptual
  argument;
- directness: direct, partial, contextual, or analogy-only;
- maturity: established, active/contested, or speculative;
- direction: supports, qualifies, challenges, neutral, or analogy-only;
- model and partition dependence;
- empirical replication or independent corroboration where applicable;
- source status: peer reviewed, preprint, book, proceedings, or other.

Interpretive frameworks are not empirical confirmation merely because they are
compatible with the synthesis.

## 9. Synthesis method

Organize synthesis claim-by-claim and comparison-dimension-by-dimension, not as
a sequence of favorable paper summaries. For each proposed cross-domain match:

1. state the source result in native terms;
2. map `H`, `M`, the admissible intervention family, and the resulting support
   `R^pi` or path law `P^pi(F)`;
3. classify the match as verbal, structural, formal, or derivational;
4. record the strongest non-equivalence;
5. compare the best rival explanation;
6. identify the highest claim level actually justified.

Avoid evidence vote-counting. The force of the synthesis depends on formal
comparability, evidence quality, and discriminatory content, not citation count.

## 10. Null and rival models

The default null is that laws, a sufficiently complete state, boundary
conditions, and interventions already determine all relevant future
distributions; "information as constraint" is then a redescription with no new
physical content. Other mandatory rivals include state augmentation or Markovian
embedding, coarse-graining or observer dependence, ordinary stability and
selection dynamics, scale-specific biological organization, and failure to
identify interventional or counterfactual laws from observational statistics.
For novelty claims, mandatory rivals also include fixed-space first discovery,
classifier/coarse-graining artifacts, reinforcement or evolving-network models
without ICP carrier succession, duplicate rediscovery, and resource-limited
search.

Rivals are tracked in `analysis/competing_explanations.csv`. ICP should be
regarded as an independently established principle only after a formal version
distinguishes itself from at least one strong rival.

## 11. Stopping rule

End broad mapping at conceptual saturation: successive searches add neither a
new mechanism, a material boundary condition, a cross-domain non-equivalence,
nor a serious rival. Continue targeted searching for unresolved pivotal claims,
contrary evidence, and missing primary sources.

## 12. Reporting

Report methods and limitations with enough detail to reproduce the search and
trace every major manuscript claim to evidence rows. Grade conclusions as
established field result, plausible synthesis inference, or ICP conjecture.
State the evidence cutoff and call closure conceptual rather than exhaustive.
List intentionally deferred searches as question-triggered work packages.
