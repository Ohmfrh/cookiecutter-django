from .base import *

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env('DJANGO_SECRET_KEY', default='!!!SET DJANGO_SECRET_KEY!!!')

DEBUG = False

ALLOWED_HOSTS = ['{{cookiecutter.domain_name}}']

# django_admin_env_notice
# ------------------------------------------------------------------------------
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#FF2222"

# Your stuff...
# ------------------------------------------------------------------------------
