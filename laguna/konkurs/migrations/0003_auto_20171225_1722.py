# Generated by Django 2.0 on 2017-12-25 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0002_auto_20171225_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time',
            field=models.DurationField(validators=[django.core.validators.MaxValueValidator(1200)]),
        ),
    ]
