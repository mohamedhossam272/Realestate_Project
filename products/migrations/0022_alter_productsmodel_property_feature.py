# Generated by Django 3.2.15 on 2022-08-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_rename_property_value_productsmodel_property_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='property_feature',
            field=models.CharField(choices=[('For Sale', 'sale'), ('For Rent', 'rent')], default='For Sell', max_length=8),
        ),
    ]
