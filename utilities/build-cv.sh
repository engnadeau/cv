#!/usr/bin/env bash

# quit script if anything fails
set -e

# echo each command
set -x

# process jinja templates
python3 generate_cv.py

# build tex
cd build/
xelatex nicholas-nadeau-cv.tex
mv nicholas-nadeau-cv.pdf nicholas-nadeau-cv-$(date +'%Y%m%d%H%M%S').pdf
cd ..
