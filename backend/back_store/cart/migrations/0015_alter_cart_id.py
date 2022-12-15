# Generated by Django 4.1.3 on 2022-12-14 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
