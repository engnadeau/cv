import os
import json


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

    resume.first_name = resume_json['basics']['name'].split()[0]
    resume.last_name = resume_json['basics']['name'].split()[1]

    resume.address = ', '.join([
        resume_json['basics']['location']['address'],
        resume_json['basics']['location']['city'],
        resume_json['basics']['location']['region'],
        resume_json['basics']['location']['countryCode'],
        resume_json['basics']['location']['postalCode']
    ])

    resume.phone = resume_json['basics']['phone']
    resume.email = resume_json['basics']['email']
    resume.site = resume_json['basics']['website']

    for profile in resume_json['basics']['profiles']:
        if 'github' in profile['network'].lower():
            resume.github = profile['username']
        elif 'linkedin' in profile['network'].lower():
            resume.linkedin = profile['username']

    return resume


def load_from_resume_json(path):
    resume_json = load_resume_json(path)
    resume = generate_from_resume_json(resume_json)
    return resume


def load_resume_json(path):
    with open(path)as f:
        resume_json = json.load(f)

    return resume_json
