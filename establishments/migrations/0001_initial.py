# Generated by Django 4.0.3 on 2022-03-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('canton', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
