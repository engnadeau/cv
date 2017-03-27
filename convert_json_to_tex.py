import json
import os

import jinja2


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

    resume = load_from_resume_json(os.path.join(root_path, 'resume.json'))

    template_path = os.path.join(root_path, 'templates')
    template = load_jinja_template(os.path.join(template_path, 'cv-template.tex'))

    with open(os.path.join(root_path, 'nnadeau-cv.tex'), 'w') as f:
        out = template.render(resume=resume)
        f.write(out)


class Resume:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone = None
        self.email = None
        self.site = None


def generate_from_resume_json(resume_json):
    resume = Resume()

    # set simple items
    resume.first_name = resume_json['basics']['name'].split()[0]
    resume.last_name = resume_json['basics']['name'].split()[1]
    resume.phone = resume_json['basics']['phone']
    resume.email = resume_json['basics']['email']
    resume.site = resume_json['basics']['website']
    resume.label = resume_json['basics']['label']
    resume.skills = resume_json['skills']
    resume.languages = resume_json['languages']
    resume.certifications = resume_json['certifications']

    resume.address = ', '.join([
        resume_json['basics']['location']['address'],
        resume_json['basics']['location']['city'],
        resume_json['basics']['location']['region'],
        resume_json['basics']['location']['countryCode'],
        resume_json['basics']['location']['postalCode']
    ])

    for profile in resume_json['basics']['profiles']:
        if 'github' in profile['network'].lower():
            resume.github = profile['username']
        elif 'linkedin' in profile['network'].lower():
            resume.linkedin = profile['username']

    # set date ordered items; ensure that "present" jobs/etc are first
    resume.education = sort_by_date(resume_json['education'])
    resume.work = sort_by_date(resume_json['work'])
    resume.volunteer = sort_by_date(resume_json['volunteer'])
    resume.awards = sort_by_date(resume_json['awards'], key='date')
    resume.presentations = sort_by_date(resume_json['presentations'])
    resume.workshops = sort_by_date(resume_json['workshops'])
    resume.projects = sort_by_date(resume_json['projects'])

    return resume


def sort_by_date(entries, key='startDate'):
    entries = sorted(entries, key=lambda d: list(map(int, d[key].split('-'))),
                     reverse=True)
    for i, e in enumerate(entries):
        if 'endDate' not in e:
            entries.insert(0, entries.pop(i))
            break

    return entries


def load_from_resume_json(path):
    resume_json = load_resume_json(path)
    resume = generate_from_resume_json(resume_json)
    return resume


def load_resume_json(path):
    with open(path)as f:
        resume_json = json.load(f)

    return resume_json


if __name__ == '__main__':
    run()
