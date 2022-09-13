.DEFAULT_GOAL := pdf

TEX_PATH := tex/cv.tex
TEX_SOURCES := $(shell find $(dir $(TEX_PATH)) -name '*.tex')

OUTPUT_DIR := out
PDF_PATH := $(OUTPUT_DIR)/nicholas-nadeau_cv.pdf

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# phony targets

.PHONY: pdf
pdf: $(PDF_PATH)

.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: debug
debug:
	@echo TEX sources: $(TEX_SOURCES)

.PHONY: docker
docker:
	docker run \
		-v $$(pwd):/$$(basename $$(pwd)) \
		-w /$$(basename $$(pwd)) \
		-it \
		texlive/texlive \
		make

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file targets

$(PDF_PATH): $(TEX_PATH) $(TEX_SOURCES) awesome-cv.cls
	mkdir -p $(OUTPUT_DIR)
	xelatex -output-directory=$(OUTPUT_DIR) $<
	mv $(OUTPUT_DIR)/$(basename $(notdir $(TEX_PATH))).pdf $(PDF_PATH)

awesome-cv.cls:
	cp awesome-cv/awesome-cv.cls .
