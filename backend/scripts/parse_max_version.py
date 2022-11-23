import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_store.settings')
import django
django.setup()

with open('max_version.json', 'r', encoding='utf-8') as f:
    all_products = json.load(f)

from shop.models import *


product = Product.objects.all()



for x in product.values():
    p = x["name"]
    if p in all_products:
        for a in all_products[p]:
            print(p, "->>>>", a['title'])
            pid = x["id"]
                # print(p, "---->", target, x["id"])
            i = ProductMaxVersion(product=Product(id=pid), title = a['title'], description = a['description'])
            i.save()
    else:
        pass
