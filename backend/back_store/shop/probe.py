import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_store.settings')
import django
django.setup()



import django
from django.conf import settings
from shop import myapp_defaults

settings.configure(default_settings=myapp_defaults, DEBUG=True)
django.setup()

# Now this script or any imported module can use any part of Django it needs.
from myapp import models



from models import *

keys = []

for p in Product.objects.all():
    print(p.attrs)