# Generated by Django 5.0.6 on 2024-07-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingListAPI', '0012_remove_customproductmodel_barcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ready_to_accept_lists',
            field=models.BooleanField(default=True),
        ),
    ]
