# Set the default goal for the Makefile
.DEFAULT_GOAL := all

# Paths and file definitions
TEX_PATH := src/cv.tex
TEX_SOURCES := $(shell find $(dir $(TEX_PATH)) -name '*.tex')
OUTPUT_DIR := out
PDF_PATH := $(OUTPUT_DIR)/nicholas-nadeau_cv.pdf
AWESOME_CV_CLASS := awesome-cv/awesome-cv.cls

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# "all" target to build everything
.PHONY: all
all: git pdf
	@echo "All targets built successfully."

# Ensure all git submodules are initialized and updated
.PHONY: git
git:
	@echo "Initializing and updating git submodules..."
	git submodule update --init --recursive
	@echo "Git submodules are up-to-date."

# Generate the PDF using LaTeX
.PHONY: pdf
pdf: $(PDF_PATH)
	@echo "PDF generated successfully at $(PDF_PATH)."

.PHONY: build
build: pdf

# Clean the output directory
.PHONY: clean
clean:
	@echo "Cleaning output directory $(OUTPUT_DIR)..."
	-rm -rf $(OUTPUT_DIR)
	@echo "Output directory cleaned."

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File targets (rules to generate files)

# Build the PDF file
$(PDF_PATH): $(TEX_PATH) $(TEX_SOURCES) $(AWESOME_CV_CLASS)
	@echo "Generating PDF from $(TEX_PATH)..."
	mkdir -p $(OUTPUT_DIR)
	xelatex -output-directory=$(OUTPUT_DIR) $<
	mv $(OUTPUT_DIR)/$(basename $(notdir $(TEX_PATH))).pdf $(PDF_PATH)
	@echo "PDF moved to final location: $(PDF_PATH)."
