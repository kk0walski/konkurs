# Generated by Django 2.0 on 2018-01-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0002_auto_20180115_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uczestnik',
            name='site',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
