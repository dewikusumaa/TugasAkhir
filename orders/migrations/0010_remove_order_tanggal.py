# Generated by Django 3.2.2 on 2021-07-23 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_tanggal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tanggal',
        ),
    ]
