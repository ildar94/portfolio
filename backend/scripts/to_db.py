import os

this_path = os.getcwd()
products_images_directory = this_path + r"\\media\\images\\products"

for product_path in os.listdir(products_images_directory):
    d = os.path.join(products_images_directory, product_path)
    if os.path.isdir(d):
        print(product_path)
