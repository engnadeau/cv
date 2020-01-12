.PHONY: pdf site

pdf:
	xelatex cv.tex
	mv cv.pdf nicholas_nadeau_cv.pdf

site: pdf
	cp nicholas_nadeau_cv.pdf site/nicholas_nadeau_cv.pdf
