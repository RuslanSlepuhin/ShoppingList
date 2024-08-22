# Generated by Django 5.0.6 on 2024-07-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingListAPI', '0011_customproductmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customproductmodel',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='customproductmodel',
            name='unit',
        ),
        migrations.AddField(
            model_name='customproductmodel',
            name='quantity',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customproductmodel',
            name='svgKey',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
