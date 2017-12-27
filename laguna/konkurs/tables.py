import django_tables2 as tables
from .models import Work


class WorkTable(tables.Table):
    
    class Meta:
        model = Work
        template = 'django_tables2/bootstrap.html'
        fields = ('pk', 'category', 'title', 'addTime')