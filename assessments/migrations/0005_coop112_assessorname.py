# Generated by Django 4.0.3 on 2022-03-29 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0004_coop112_alter_coop11_versefull'),
    ]

    operations = [
        migrations.AddField(
            model_name='coop112',
            name='assessorname',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]