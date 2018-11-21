from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    '{{cookiecutter.project_slug}}.functional_tests'
]