# Generated by Django 4.0.3 on 2022-03-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0003_alter_establishments_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishments',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='establishments',
            name='telephone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]