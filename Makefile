.PHONY: pdf-cover
pdf-cover:
	xelatex cover-letter.tex

.PHONY: pdf-cv
pdf-cv:
	xelatex cv.tex
	mv cv.pdf nicholas_nadeau_cv.pdf

.PHONY: pdf
pdf: pdf-cv pdf-cover

.PHONY: site
site: pdf
	cp nicholas_nadeau_cv.pdf site/nicholas_nadeau_cv.pdf
