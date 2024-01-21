# Generated by Django 3.2.15 on 2022-08-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_productsmodel_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='Images',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='property_value',
            field=models.CharField(choices=[('For Sell', 'sell'), ('For Rent', 'rent')], default='For Sell', max_length=8),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='property_type',
            field=models.CharField(choices=[('Apartment', 'apartment'), ('House', 'house'), ('Studio', 'studio')], default='Apartment', max_length=9),
        ),
    ]
