# Generated by Django 4.1.3 on 2022-11-02 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_productstatus_products_stock_picture_cart_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products_Stock',
            new_name='ProductsStock',
        ),
    ]
