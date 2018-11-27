from .base import *


SECRET_KEY = env('DJANGO_SECRET_KEY', default='!!!SET DJANGO_SECRET_KEY!!!')

DEBUG = False

ALLOWED_HOSTS = ['{{cookiecutter.domain_name}}']

STATIC_ROOT = 'static_prod'
