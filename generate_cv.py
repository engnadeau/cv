import logging
from pathlib import Path

import jinja2
import yaml


def load_latex_template(path: Path):
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(path.parent.resolve())),
        block_start_string='\B{',
        block_end_string='}',
        variable_start_string='\V{',
        variable_end_string='}',
        comment_start_string='\C{',
        comment_end_string='}',
    )
    template = environment.get_template(path.name)

    return template


def load_html_template(path: Path):
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(path.parent.resolve())),
    )
    template = environment.get_template(path.name)

    return template


def run():
    # load data
    root_dir = Path(__file__).parent
    cv_data_path = root_dir / 'cv.yaml'  # type: Path
    logging.info(f'Loading {cv_data_path.resolve()}')
    with open(cv_data_path) as f:
        cv_data = yaml.load(f)

    # load latex template
    template_path = root_dir / 'templates' / 'cv-template.tex'  # type: Path
    logging.info(f'Loading template: {template_path.resolve()}')
    template = load_latex_template(template_path)

    # generate cv
    build_dir = root_dir / 'build'  # type: Path
    cv_tex_path = build_dir / f'nicholas-nadeau-cv.tex'
    logging.info(f'Exporting tex: {cv_tex_path.resolve()}')
    with open(cv_tex_path, 'w') as f:
        out = template.render(cv=cv_data)
        f.write(out)

    # load html template
    template_path = root_dir / 'templates' / 'index-template.html'  # type: Path
    logging.info(f'Loading template: {template_path.resolve()}')
    template = load_html_template(template_path)

    # generate cv
    site_dir = root_dir / 'site'  # type: Path
    index_path = site_dir / 'index.html'
    logging.info(f'Exporting tex: {index_path.resolve()}')
    with open(index_path, 'w') as f:
        out = template.render(cv=cv_data)
        f.write(out)

    logging.info('Generation complete')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
