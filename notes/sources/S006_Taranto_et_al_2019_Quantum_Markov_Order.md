# S006 — Taranto et al. (2019), Quantum Markov Order

## Bibliographic record

- Citation key: `TarantoEtAl2019MarkovOrder`
- DOI: <https://doi.org/10.1103/PhysRevLett.122.140401>
- Status: peer-reviewed theoretical article
- Stratum: quantum memory and process tensors

## Why included

Provides the strongest theorem-level warning against treating memory length as
an intrinsic, intervention-independent property.

## Native result and formalism

Finite quantum Markov order is defined by conditional independence between
history and future after an instrument is applied within a memory block. A
non-Markovian process with finite order is generally finite only relative to a
specific instrument; finite order for all instruments is essentially Markovian.

## Common-schema mapping

- `H`: process before the memory block.
- `M`: the memory block plus its selected instrument.
- `Pi`: memory instruments and future operations.
- Future object: conditional multitime process.
- Claim type: intervention-relative operational independence.

## Assumptions, limitations, and rival reading

Different probes expose different memory. Conditional mutual information alone
has quantum caveats, and approximate order needs a declared tolerance. The
result favors a relational `M(Pi, A)` over an intrinsic scalar memory.

## Locators and links

- p. 2, generalized Born rule Eq. (3), order definition Eq. (4), factorization
  Eq. (5).
- p. 3, Theorem 4 and instrument-specific discussion; pp. 3–4, approximation
  caveats.
- Claim: `C008`; rivals: `R002`, `R003`; criteria: `F003`, `F006`.

