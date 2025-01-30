<!-- PROJECT SHIELDS -->
[![Build](https://github.com/engnadeau/cv/actions/workflows/build.yml/badge.svg)](https://github.com/engnadeau/cv/actions/workflows/build.yml)

# Nicholas Nadeau's CV

[**➡️➡️ Get the latest version of my CV (PDF) ⬅️⬅️**](https://engnadeau.github.io/cv/nicholas-nadeau_cv.pdf)

This repository contains the source code for my CV, automatically built using LaTeX, Docker, and GitHub Actions.

## Build Instructions

### Prerequisites

* **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
* **Remote - Containers VS Code Extension:** Install the "Remote - Containers" extension in VS Code.

### Building the CV

1. **Open the folder:** Open the `cv` folder in VS Code.

2. **Reopen in Container:** Click the green "Reopen in Container" button in the bottom-left corner of VS Code.  This will build and start a Docker container based on the configuration in `.devcontainer/devcontainer.json`.

3. **Build:** Once the container is running, open a terminal and run `make pdf`. The generated PDF will be located in the `out/` directory.

## Makefile

The [`Makefile`](./Makefile) provides:

- `make pdf`: Generates the PDF.
- `make clean`: Cleans the output directory.

## Deployment

- The `master` branch is automatically built, tagged, and deployed by GitHub Actions.
- The generated PDF is uploaded as a release asset and deployed to GitHub Pages.
