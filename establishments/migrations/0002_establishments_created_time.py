# Generated by Django 4.0.3 on 2022-03-14 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishments',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
