# Generated by Django 2.0 on 2017-12-22 16:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
import konkurs.models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0002_auto_20171217_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konkurs.Work'),
        ),
        migrations.AlterField(
            model_name='uczestnik',
            name='birthday',
            field=models.DateField(default=datetime.date.today, validators=[konkurs.models.MinAgeValidator(18)]),
        ),
        migrations.AlterField(
            model_name='video',
            name='time',
            field=models.DurationField(),
        ),
    ]