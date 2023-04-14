# Nicholas' CV

[**➡️➡️ Get the latest version ⬅️⬅️**](https://engnadeau.github.io/cv/nicholas-nadeau_cv.pdf)

My personal CV that's automatically generated using the following tech stack:

- LaTeX + XeTeX for document writing and PDF generation
- GitHub Actions for automated CI/CD
- Docker for a consistent development environment and CI image
- GitHub Pages + Jamstack for deployment and hosting

| Item   | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Repo   | ![GitHub repo size](https://img.shields.io/github/repo-size/engnadeau/cv) ![GitHub](https://img.shields.io/github/license/engnadeau/cv) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/engnadeau/cv)                                                                                                                                                                                                                                                                          |
| CI     | [![Build](https://github.com/engnadeau/cv/actions/workflows/build.yml/badge.svg)](https://github.com/engnadeau/cv/actions/workflows/build.yml) [![Release](https://github.com/engnadeau/cv/actions/workflows/release.yml/badge.svg)](https://github.com/engnadeau/cv/actions/workflows/release.yml) [![pages-build-deployment](https://github.com/engnadeau/cv/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/engnadeau/cv/actions/workflows/pages/pages-build-deployment) |
| Social | ![GitHub followers](https://img.shields.io/github/followers/engnadeau?style=social) ![Twitter Follow](https://img.shields.io/twitter/follow/engnadeau?style=social)                                                                                                                                                                                                                                                                                                                                       |

## Requirements

### Docker Development (Recommended)

```bash
# Run the container
docker run --rm -it -v $(pwd):/app -w /app --entrypoint /bin/bash texlive/texlive
```

### Local Development

```bash
# Install TeX Live
sudo apt install texlive-full texlive-xetex
```

## Usage

- See the [`Makefile`](./Makefile) for entrypoints

## Deployments

- `master` branch is automatically built, tagged, and deployed by GitHub Actions
- The PDF is uploaded as an asset to a static site hosted by GitHub Pages
