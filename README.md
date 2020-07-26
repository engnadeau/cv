![Build and Publish](https://github.com/nnadeau/cv/workflows/Build%20and%20Publish/badge.svg)

# CV

My personal CV.
Get the latest version [here](https://nnadeau.github.io/cv/).

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

- [Master branch](https://github.com/nnadeau/cv/tree/master) is built by [Travis CI](https://github.com/nnadeau/cv/blob/master/.travis.yml) and deployed to [GH Pages](https://nnadeau.github.io/cv/)
- The PDF is uploaded as an asset to the static site

## Bugs

- https://github.com/posquit0/Awesome-CV/issues/234
