# Generated by Django 4.1.2 on 2022-10-30 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_slug_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_attrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
        ),
    ]
