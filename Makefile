.PHONY: pdf

pdf: render
	latexmk -pdf cv.tex
	mv cv.pdf nicholas_nadeau_cv_$(date +'%Y-%m-%d').pdf
