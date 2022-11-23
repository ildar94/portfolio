# Generated by Django 4.1.2 on 2022-11-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_products_stock_productsstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_option',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_option2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_option3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_variants',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_variants2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='productadditionals',
            name='prod_variants3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='productadditionals',
            name='product',
        ),
        migrations.AddField(
            model_name='productadditionals',
            name='product',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]
