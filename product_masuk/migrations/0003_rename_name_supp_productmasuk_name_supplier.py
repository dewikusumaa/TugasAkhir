# Generated by Django 3.2.2 on 2021-07-31 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_masuk', '0002_productmasuk_adrress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmasuk',
            old_name='name_supp',
            new_name='name_supplier',
        ),
    ]