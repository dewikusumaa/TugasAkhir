# Generated by Django 3.2.2 on 2021-07-22 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_keluar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productkeluar',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productkeluar',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
