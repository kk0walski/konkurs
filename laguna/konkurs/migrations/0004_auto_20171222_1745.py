# Generated by Django 2.0 on 2017-12-22 16:45

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0003_auto_20171222_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uczestnik',
            name='cellphone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
        migrations.AlterField(
            model_name='uczestnik',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
