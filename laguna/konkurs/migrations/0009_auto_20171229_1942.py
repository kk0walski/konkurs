# Generated by Django 2.0 on 2017-12-29 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0008_auto_20171229_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 19, 42, 40, 742221)),
        ),
    ]
