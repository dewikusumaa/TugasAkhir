# Generated by Django 3.2.2 on 2021-07-22 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210721_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cust_id',
            new_name='cust_kode',
        ),
    ]