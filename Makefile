.PHONY: render pdf dirs clean

clean:
	rm -rf build/

build-dir: clean
	mkdir -p build/pdf/
	mkdir -p build/site/
	cp -a modules/Awesome-CV/fonts/ build/pdf/fonts/
	cp modules/Awesome-CV/awesome-cv.cls build/pdf/
	cp modules/Awesome-CV/fontawesome.sty build/pdf/
	cp -a Skeleton/css/ build/site/
	cp static/custom.css build/site/
	cp static/favicon.ico build/site/

render: build-dir
	pipenv run python scripts/render_templates.py

pdf: render
	cd build/pdf/ && \
		xelatex cv.tex && \
		mv cv.pdf nicholas_nadeau_cv_$(date +'%Y-%m-%d').pdf
