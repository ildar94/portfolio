# Generated by Django 4.1.3 on 2022-12-13 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ff5577f3-195d-4da4-89cf-0d394012a47e'), primary_key=True, serialize=False),
        ),
    ]