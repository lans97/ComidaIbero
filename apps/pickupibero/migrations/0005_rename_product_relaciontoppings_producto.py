# Generated by Django 4.2.6 on 2023-11-29 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pickupibero', '0004_alter_ordenitem_parentitem_relaciontoppings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relaciontoppings',
            old_name='product',
            new_name='producto',
        ),
    ]