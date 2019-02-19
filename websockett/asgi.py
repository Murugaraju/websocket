import os
import django
import channels.routing import get_default_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE","websockett.settings")
django.setup()
application=get_default_application()