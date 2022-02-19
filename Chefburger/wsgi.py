"""
WSGI config for Chefburger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chefburger.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR,"static/"))

