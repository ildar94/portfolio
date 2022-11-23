# Generated by Django 4.1.2 on 2022-11-01 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_attrs_category_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAdditionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complectation', models.JSONField(blank=True, null=True)),
                ('colors', models.JSONField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_option', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_variants', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_option2', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_variants2', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_option3', models.CharField(blank=True, max_length=100, null=True)),
                ('prod_variants3', models.CharField(blank=True, max_length=100, null=True)),
                ('editions', models.JSONField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
