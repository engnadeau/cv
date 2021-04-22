.DEFAULT_GOAL := pdf

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# latex build

.PHONY: pdf
pdf: pdf-cv pdf-cover

.PHONY: pdf-cover
pdf-cover: awesome-cv-files
	mkdir -p out
	xelatex -output-directory=out tex/cover-letter.tex

.PHONY: pdf-cv
pdf-cv: awesome-cv-files
	mkdir -p out
	xelatex -output-directory=out tex/cv.tex

.PHONY: awesome-cv-files
awesome-cv-files:
	cp awesome-cv/awesome-cv.cls .
	cp awesome-cv/fontawesome.sty .
	cp -r awesome-cv/fonts/ .

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# site deployment

.PHONY: site
site: pdf-cv
	cp out/cv.pdf site/nicholas-nadeau_cv.pdf
