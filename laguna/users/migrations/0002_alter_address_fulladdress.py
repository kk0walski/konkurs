# Generated by Django 3.2.6 on 2021-08-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='fullAddress',
            field=models.CharField(max_length=1024, verbose_name='Full address'),
        ),
    ]
