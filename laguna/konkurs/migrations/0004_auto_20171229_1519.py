# Generated by Django 2.0 on 2017-12-29 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0003_auto_20171227_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sculpture',
            name='video_password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='virtualart',
            name='video_password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 15, 19, 9, 308248)),
        ),
    ]
