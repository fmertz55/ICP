# BioSystems submission package

Primary manuscript source:

- `manuscript/submission_main.tex`

Build from the repository root with:

```sh
make submission
```

The resulting review PDF is:

- `output/pdf/icp_biosystems_submission.pdf`

The same target also creates the submission-source artifacts:

- `output/submission/icp_biosystems_sources.zip`
- `output/submission/icp_biosystems_sources.zip.sha256`
- `output/pdf/icp_biosystems_submission.pdf.sha256`
- `output/submission/icp_biosystems_build_manifest.json`

The ZIP contains the journal-facing master, every referenced section source,
the BibTeX database, and the support files in this directory. Members are
sorted and carry fixed timestamps and permissions, so an unchanged source tree
produces the same archive hash. The JSON manifest records hashes for every
packaged input, the build scripts, the PDF and ZIP, together with the Git commit,
branch, and source-path status used for the build. Verify the complete artifact
set independently with:

```sh
python3 scripts/validate_icp_submission.py --artifacts
```

The submission is intentionally figure-free. BioSystems' current author guide
prohibits generative-AI-created or AI-altered artwork, so no AI-assisted figure
source or rendered figure is included in either the manuscript or the source
ZIP. `highlights.txt`, the presubmission inquiry, the cover letter, and the final
administrative checklist are stored in this directory.

The source is intentionally submission-neutral rather than dependent on a
locally unavailable publisher class. BioSystems permits a consistent reference
style at initial submission and accepts editable LaTeX sources. On acceptance,
migrate the same content to the then-current Elsevier production template if
requested.
