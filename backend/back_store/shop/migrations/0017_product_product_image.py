# Generated by Django 4.1.3 on 2022-11-14 11:17

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_aboutproduct_alter_picture_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.product_directory_path),
        ),
    ]