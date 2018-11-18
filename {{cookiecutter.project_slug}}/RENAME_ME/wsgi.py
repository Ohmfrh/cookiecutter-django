# TODO: Update Docstring
"""
WSGI config for RENAME_ME project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: Update with new settings layout
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RENAME_ME.settings')

application = get_wsgi_application()
