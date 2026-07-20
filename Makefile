LATEXMK := latexmk
LATEXFLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error
BUILD := tmp/latex
OUT := output/pdf

.PHONY: all technical lay clean

all: technical lay

technical:
	mkdir -p $(BUILD)/technical $(OUT)
	$(LATEXMK) $(LATEXFLAGS) -outdir=$(BUILD)/technical manuscript/technical_main.tex
	cp $(BUILD)/technical/technical_main.pdf $(OUT)/iota_icp_scientific_synthesis.pdf

lay:
	mkdir -p $(BUILD)/lay $(OUT)
	$(LATEXMK) $(LATEXFLAGS) -outdir=$(BUILD)/lay manuscript/lay_main.tex
	cp $(BUILD)/lay/lay_main.pdf $(OUT)/how_the_past_changes_what_can_happen_next.pdf

clean:
	$(LATEXMK) -C -outdir=$(BUILD)/technical manuscript/technical_main.tex
	$(LATEXMK) -C -outdir=$(BUILD)/lay manuscript/lay_main.tex
