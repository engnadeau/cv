#!/usr/bin/env bash

# quit script if anything fails
set -e

# echo each command
set -x

# prep build dir
mkdir -p build
cp -a Awesome-CV/fonts/ build/fonts/
cp Awesome-CV/awesome-cv.cls build/
cp Awesome-CV/fontawesome.sty build/

# prep site dir
cp -a Skeleton/css site/
