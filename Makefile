.DEFAULT_GOAL := pdf

TEX_PATH := tex/cv.tex
TEX_SOURCES := $(shell find $(dir $(TEX_PATH)) -name '*.tex')

OUTPUT_DIR := out
PDF_PATH := $(OUTPUT_DIR)/nicholas-nadeau_cv.pdf

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# phony targets

.PHONY: pdf
pdf: $(PDF_PATH)

.PHONY: site
site: pdf
	cp $(PDF_PATH) site/$(PDF_FNAME)

.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: debug
debug:
	@echo TEX sources: $(TEX_SOURCES)

.PHONY: documentclass
documentclass:
	cp awesome-cv/awesome-cv.cls .

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file targets

$(PDF_PATH): $(TEX_PATH) $(TEX_SOURCES) documentclass
	mkdir -p $(OUTPUT_DIR)
	xelatex -output-directory=$(OUTPUT_DIR) $<
	mv $(OUTPUT_DIR)/$(basename $(notdir $(TEX_PATH))).pdf $(PDF_PATH)
