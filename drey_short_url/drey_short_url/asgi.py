"""
ASGI config for drey_short_url project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

"""
drey_short_url is the main installation folder of Djago, so all files in this folder are created automatically
Most of his files will not be modified except for a few, I will add comments so you can see my changes and their explanations
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drey_short_url.settings')

application = get_asgi_application()
