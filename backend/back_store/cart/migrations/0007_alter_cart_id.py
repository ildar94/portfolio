# Generated by Django 4.1.3 on 2022-12-13 15:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fed9eef3-774d-4de0-ab64-a50f3aab03e6'), primary_key=True, serialize=False),
        ),
    ]
