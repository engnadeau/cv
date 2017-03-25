import jinja2
import os

from py.resume import load_from_resume_json


def load_jinja_template(path):
    latex_jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(path)),
        block_start_string='\B{',
        block_end_string='}',
        variable_start_string='\V{',
        variable_end_string='}',
        comment_start_string='\C{',
        comment_end_string='}',
    )
    template = latex_jinja_env.get_template(os.path.basename(path))

    return template


def run():
    root_path = os.path.dirname(__file__)
    root_path = os.path.dirname(root_path)

    resume = load_from_resume_json(os.path.join(root_path, 'resume.json'))

    template_path = os.path.join(root_path, 'templates')
    template = load_jinja_template(os.path.join(template_path, 'cv-template.tex'))

    with open(os.path.join(root_path, 'cv.tex'), 'w') as f:
        f.write(template.render(resume=resume))


if __name__ == '__main__':
    run()
