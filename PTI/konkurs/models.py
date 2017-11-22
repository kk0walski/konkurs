import os

from django.db import models

from .validators import only_pdf

from datetime import datetime
from datetime import date
# Create your models here.


def directory_path(instance, filename):
    return os.path.join(instance.competition.id, instance.id, filename)


def my_date(myYear, myMonth, myDay):
    return date(year=myYear, month=myMonth, day=myDay)


class Registration(models.Model):
    author = models.ForeignKey('Author')
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    work = models.FileField(upload_to=directory_path, validators=[only_pdf])
    survey = models.FileField(upload_to=directory_path, validators=[only_pdf])
    certification = models.FileField(
        upload_to=directory_path, validators=[only_pdf])
    attachements = models.FileField(upload_to=directory_path)
    accepted = models.BooleanField()


class Competition(models.Model):
    year = models.IntegerField(primary_key=True, default=date.today().year+1)
    beginDate = models.DateField(default=my_date(date.today().year+1, 10, 1))
    endDate = models.DateField(default=my_date(date.today().year+1, 5, 20))
    reasultDate = models.DateField(default=my_date(date.today().year+1, 10, 31))
    plakat = models.FileField(upload_to=directory_path)
    regulamin = models.FileField(upload_to=directory_path)

class Author(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    birthday = models.DateField()