.PHONY: pdf
pdf:
	xelatex cv.tex
	mv cv.pdf nicholas_nadeau_cv.pdf

.PHONY: site
site: pdf
	cp nicholas_nadeau_cv.pdf site/nicholas_nadeau_cv.pdf
