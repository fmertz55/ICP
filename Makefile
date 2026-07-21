LATEXMK := latexmk
LATEXFLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error
PYTHON ?= python3
BUILD := tmp/latex
OUT := output/pdf
SUBMISSION_OUT := output/submission

.PHONY: all technical submission lay clean

all: technical submission lay

technical:
	mkdir -p $(BUILD)/technical $(OUT)
	$(LATEXMK) $(LATEXFLAGS) -outdir=$(BUILD)/technical manuscript/technical_main.tex
	cp $(BUILD)/technical/technical_main.pdf $(OUT)/iota_icp_scientific_synthesis.pdf

submission:
	mkdir -p $(BUILD)/submission $(OUT) $(SUBMISSION_OUT)
	$(LATEXMK) $(LATEXFLAGS) -outdir=$(BUILD)/submission manuscript/submission_main.tex
	cp $(BUILD)/submission/submission_main.pdf $(OUT)/icp_biosystems_submission.pdf
	$(PYTHON) scripts/validate_icp_submission.py
	$(PYTHON) scripts/package_icp_submission.py
	$(PYTHON) scripts/validate_icp_submission.py --artifacts

lay:
	mkdir -p $(BUILD)/lay $(OUT)
	$(LATEXMK) $(LATEXFLAGS) -outdir=$(BUILD)/lay manuscript/lay_main.tex
	cp $(BUILD)/lay/lay_main.pdf $(OUT)/how_the_past_changes_what_can_happen_next.pdf

clean:
	$(LATEXMK) -C -outdir=$(BUILD)/technical manuscript/technical_main.tex
	$(LATEXMK) -C -outdir=$(BUILD)/submission manuscript/submission_main.tex
	$(LATEXMK) -C -outdir=$(BUILD)/lay manuscript/lay_main.tex
