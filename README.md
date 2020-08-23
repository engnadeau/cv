<br />
<p align="center">
<a href="https://github.com/nnadeau/cv">
<img src="https://raw.githubusercontent.com/nnadeau/cv/master/media/logo.png" alt="Logo" width="80">
</a>

<h3 align="center">CV</h3>

<p align="center">
LaTeX + GitHub Actions + Jamstack automated professional CV
<br />
<a href="https://nnadeau.github.io/cv/"><strong>Get the latest version</strong></a>
<br />
</p>
</p>

![Build and Publish](https://github.com/nnadeau/cv/workflows/Build%20and%20Publish/badge.svg)

[![GitHub issues](https://img.shields.io/github/issues/nnadeau/cv)](https://github.com/nnadeau/cv/issues)
[![GitHub forks](https://img.shields.io/github/forks/nnadeau/cv)](https://github.com/nnadeau/cv/network)
[![GitHub stars](https://img.shields.io/github/stars/nnadeau/cv)](https://github.com/nnadeau/cv/stargazers)
[![GitHub license](https://img.shields.io/github/license/nnadeau/cv)](https://github.com/nnadeau/cv/blob/master/LICENSE)

[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fnnadeau%2Fcv)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fnnadeau%2Fcv)

## Requirements

- `texlive-full`
- `texlive-xetex`

## Usage

```bash
# build pdf
make pdf

# build static site
make site
```

## Deployments

- Master branch is automatically built and deployed
- The PDF is uploaded as an asset to the static site
