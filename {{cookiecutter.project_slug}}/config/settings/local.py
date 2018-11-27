from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['django_extensions']

INSTALLED_APPS += ['{{cookiecutter.project_slug}}.functional_tests']
INSTALLED_APPS += ['{{cookiecutter.project_slug}}.test_app']

CELERY_BEAT_SCHEDULE['test-task1'] = {
    'task': '{{cookiecutter.project_slug}}.test_app.tasks.task1',
    'schedule': 10,
}

CELERY_BEAT_SCHEDULE['test-task2'] = {
    'task': '{{cookiecutter.project_slug}}.test_app.tasks.task2',
    'schedule': 60,
}
