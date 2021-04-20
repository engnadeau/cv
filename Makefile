.DEFAULT_GOAL := pdf

.PHONY: pdf-cover
pdf-cover:
	xelatex cover-letter.tex
	mv cover-letter.pdf nicholas-nadeau_cover-letter.pdf

.PHONY: pdf-cv
pdf-cv:
	xelatex cv.tex
	mv cv.pdf nicholas-nadeau_cv.pdf

.PHONY: pdf
pdf: pdf-cv pdf-cover

.PHONY: site
site: pdf
	cp nicholas-nadeau_cv.pdf site/nicholas-nadeau_cv.pdf
