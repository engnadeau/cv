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


def run():
    # load data
    root_dir = Path(__file__).parent
    cv_data_path = root_dir / 'cv.yaml'  # type: Path
    logging.info(f'Loading {cv_data_path.resolve()}')
    with open(cv_data_path) as f:
        cv_data = yaml.load(f)

    # load jinja
    template_path = root_dir / 'templates' / 'cv-template.tex'  # type: Path
    logging.info(f'Loading template: {template_path.resolve()}')
    template = load_latex_template(template_path)

    # generate cv
    build_dir = root_dir / 'build'  # type: Path
    build_dir.mkdir(exist_ok=True)
    cv_tex_path = build_dir / 'nicholas-nadeau-cv.tex'
    logging.info(f'Exporting tex: {cv_tex_path.resolve()}')
    with open(cv_tex_path, 'w') as f:
        out = template.render(cv=cv_data)
        f.write(out)
    logging.info('Generation complete')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
