# Generated by Django 3.2.15 on 2022-08-26 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20220826_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsmodel',
            old_name='Images',
            new_name='images',
        ),
    ]