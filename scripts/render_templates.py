import logging
from pathlib import Path

import jinja2
import toml

ROOT_DIR = Path(__file__).parents[1]
TEMPLATES_DIR = ROOT_DIR / "templates"
BUILD_DIR = ROOT_DIR / "build"
PDF_DIR = BUILD_DIR / "pdf"
SITE_DIR = BUILD_DIR / "site"

CV_PATH = ROOT_DIR / "cv.toml"
TEX_TEMPLATE_PATH = TEMPLATES_DIR / "template.tex"
HTML_TEMPLATE_PATH = TEMPLATES_DIR / "template.html"
TEX_OUTPUT_PATH = PDF_DIR / "cv.tex"
HTML_OUTPUT_PATH = SITE_DIR / "index.html"


def load_latex_template(path: Path):
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(path.parent.resolve())),
        block_start_string="\B{",
        block_end_string="}",
        variable_start_string="\V{",
        variable_end_string="}",
        comment_start_string="\C{",
        comment_end_string="}",
    )
    template = environment.get_template(path.name)

    return template


def load_html_template(path: Path):
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(path.parent.resolve()))
    )
    template = environment.get_template(path.name)

    return template


def render_html(data: dict):
    logging.info(f"Loading template: {HTML_TEMPLATE_PATH.relative_to(ROOT_DIR)}")
    template = load_html_template(HTML_TEMPLATE_PATH)

    logging.info(f"Exporting: {HTML_OUTPUT_PATH.relative_to(ROOT_DIR)}")
    with open(HTML_OUTPUT_PATH, "w") as f:
        out = template.render(data=data)
        f.write(out)


def render_tex(data: dict):
    logging.info(f"Loading template: {TEX_TEMPLATE_PATH.relative_to(ROOT_DIR)}")
    template = load_latex_template(TEX_TEMPLATE_PATH)

    logging.info(f"Exporting: {TEX_OUTPUT_PATH.relative_to(ROOT_DIR)}")
    with open(TEX_OUTPUT_PATH, "w") as f:
        out = template.render(data=data)
        f.write(out)


def main():
    logging.info(f"Loading {CV_PATH.relative_to(ROOT_DIR)}")
    with open(CV_PATH) as f:
        data = toml.load(f)

    render_tex(data)
    render_html(data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
