# Generated by Django 3.2.2 on 2021-08-01 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210802_0532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
