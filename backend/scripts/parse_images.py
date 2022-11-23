import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_store.settings')
import django
django.setup()

with open('mydata.json', 'r', encoding='utf-8') as f:
    all_products = json.load(f)

from shop.models import *

print(len(all_products))
product = Product.objects.all()
#image = Picture.objects.all()


for x in product.values():
    p = x["name"]
    if p in all_products:
        for path in all_products[p]:
                target = "images/products/" + path
                pid = x["id"]
                print(p, "---->", target, x["id"])
                image = Picture(images=target, product=Product(id=pid))
                image.save()
    else:
        pass

# for b in all_products:
#     #print(b, "->>>>", all_products[b])
#     try:
#         c = Product.objects.get(name=b)
#         print(c)
#         for path in all_products[b]:
#             target = "images/products/" + path
#             print(b, "---->", target)
#     except DoesNotExist:
#         print("not exist")

#images/products/kugoo-c1/6_gGb9ffJ.jpg
#'Kugoo-HX-Pro/hx_pro.



#KugooKirin M4 Pro 18 Ah
#Kugoo M4 Pro 18 Ah