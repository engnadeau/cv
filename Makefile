.PHONY: pdf

pdf: 
	xelatex cv.tex
	mv cv.pdf nicholas_nadeau_cv_$(shell date +%Y-%m-%d).pdf
