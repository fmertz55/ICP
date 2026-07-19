# S026 — Corominas-Murtra, Hanel, and Thurner (2015), Sample-Space Reduction

## Bibliographic record

- Citation key: `CorominasMurtraEtAl2015SSR`
- DOI: <https://doi.org/10.1073/pnas.1420946112>
- Status: peer-reviewed theory and simulation
- Stratum: Zipf mechanisms; history-dependent reachable support

## Why included

Closest literal formal neighbor to the ICP idea that realized history restricts
counterfactual successor states.

## Native result

In the canonical walk, state `i` permits only successors below `i` until reset.
Repeated visits yield Zipf occupation. Mixing reducing and unrestricted moves
produces a power law whose exponent follows the reduction/noise mixture.

## Common-schema mapping

- `H`: realized downward path since reset.
- `M`: current state and nested remaining successor set.
- Future law: directional support-restricted transition distribution.
- ICP status: direct candidate mechanism; physical embodiment not supplied.

## Limitations and rival reading

Total order, downward motion, and reset are constructed. Real systems loop,
expand, and reopen options. Similar nestedness can reflect static topology.

## Locators and linked IDs

- Eqs. 1–6; Figs. 1–5.
- Claims: `C028`, `C032`, `C040`; rival: `R013`; criterion: `F012`.
