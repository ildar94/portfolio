# Generated by Django 4.1.2 on 2022-10-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_attr_value_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_attrs',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='attr_value',
        ),
        migrations.AddField(
            model_name='product',
            name='attrs',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='product_attr_value',
        ),
        migrations.DeleteModel(
            name='product_attrs',
        ),
    ]
