# Generated by Django 4.2.6 on 2023-11-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickupibero', '0005_rename_product_relaciontoppings_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto_imagenes/'),
        ),
    ]
