# Generated by Django 3.2.2 on 2021-08-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMasuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bahan', models.CharField(db_index=True, max_length=200)),
                ('name_supplier', models.CharField(db_index=True, max_length=200)),
                ('address', models.TextField(blank=True)),
                ('total', models.IntegerField()),
                ('satuan', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
