import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_store.settings')
import django
django.setup()

with open('elektrosamokat.json', 'r', encoding='utf-8') as f:
    all_products = json.load(f)

from models import *


def komplectation_func(product):
    komplectation_dict ={}
    title_options = product['json_options'].split('[')[1]
    title_option = title_options.split('{"title":"')[1]
    if title_option.startswith('Цвет'):
        komplectation_tmp = product['json_options'].split('[')[3]
        kompl = komplectation_tmp.split(']')[0]
        komp_tmp = kompl.replace('"', '').split(',')
        komplectation_dict['Комплектация:'] = komp_tmp
    elif title_option.startswith('Комплектация'):
        komplectation_tmp = product['json_options'].split('[')[2]
        kompl = komplectation_tmp.split(']')[0]
        komp_tmp = kompl.replace('"', '').split(',')
        komplectation_dict['Комплектация:'] =komp_tmp


    return komplectation_dict


def color_is_exist(product):
    title_options = product['json_options'].split('[')[1]
    title_option = title_options.split('{"title":"')[1]
    if title_option.startswith('Цвет'):
        color_tmp = product['json_options'].split('[')[2]
        color = color_tmp.split(']')[0]
    else:
        color = None
    return color


def exist_in(keyname,product):
    if keyname in product:
        value = product[keyname]
    else:
        value = None
    return value


def prod_option_check(product):
    prod_option = exist_in('prod_option', product)

    if prod_option != None:
        prod_variants = product['prod_variants']
    else:
        prod_variants = None

    prod_option2 = exist_in('prod_option2', product)

    if prod_option2 != None:
        prod_variants2 = product['prod_variants2']
    else:
        prod_variants2 = None

    prod_option3 = exist_in('prod_option3', product)

    if prod_option3 != None:
        prod_variants3 = product['prod_variants3']
    else:
        prod_variants3 = None
    return prod_option, prod_variants, prod_option2, prod_variants2,prod_option3, prod_variants3


def buld_editions(product):
    editions_dict ={}
    edittions = product['editions']
    for index, ed in enumerate(edittions):
        if edittions[index]['Купить в рассрочку/кредит:'] == "Нет":
            editions_dict[edittions[index]['Комплектация:']] ={'price': edittions[index]['price'], 'priceold': edittions[index]['priceold'],
                                   'sku' : edittions[index]['sku'],
                                    'Комплектация:' : edittions[index]['Комплектация:']
                                   }
    return editions_dict


def build_characteristics(product):
    characteristics_dict = {}
    characteristics = product['characteristics']
    for index, ed in enumerate(characteristics):
        char_key = characteristics[index]['title']
        char_val = characteristics[index]['value']
        characteristics_dict[char_key] = char_val
    return characteristics_dict


#
# to_json = []
# ready_dict ={}
# index = 234678
# for product in all_products:
#     name = product['title'].split("(")[0]  # в БД -charfield
#     price = product['price']  # to DB - float
#     complectation = komplectation_func(product)  # to DB JSONField
#     colors = color_is_exist(product)  # to DB JSONField
#     brand = exist_in('brand', product)  # в БД -charfield
#     prod_option_results = prod_option_check(product)  # calulating
#     prod_option = prod_option_results[0]  # в БД -charfield
#     prod_variants = prod_option_results[1]  # в БД -charfield
#     prod_option2 = prod_option_results[2]  # в БД -charfield
#     prod_variants2 = prod_option_results[3]  # в БД -charfield
#     prod_option3 = prod_option_results[4]  # в БД -charfield
#     prod_variants3 = prod_option_results[5]  # в БД -charfield
#     editions = buld_editions(product)  # to DB JSONField
#     attributes = build_characteristics(product)  # to DB JSONField
#     index +=1
#     a = Product(name = name,
#                 article = index,
#                 price = price,
#                 description = None,
#                 sales_price = None,
#                 sold_time = None,
#                 category_id = Category(name='Электросамокаты'),
#                 attrs = attributes)
#     a.save()
#     b = ProductAdditionals(
#         product=Product(name=name),
#         complectation = complectation,
#         colors = colors,
#         brand = brand,
#         prod_option = prod_option,
#         prod_variants = prod_variants,
#         prod_option2 = prod_option2,
#         prod_variants2 =prod_variants2,
#         prod_option3 = prod_option3,
#         prod_variants3 = prod_variants3,
#         editions = editions
#     )
#     b.save()



#print(to_json)
#
# with open("mydata.json", "w",  encoding='utf8') as final:
#    json.dump(to_json, final, ensure_ascii=False)