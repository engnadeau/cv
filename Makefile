.PHONY: pdf

pdf: 
	xelatex cv.tex
	cp cv.pdf nicholas_nadeau_cv.pdf

site: pdf
	cp nicholas_nadeau_cv.pdf site/nicholas_nadeau_cv.pdf
