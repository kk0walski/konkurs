import django_tables2 as tables
from .models import Work

class WorkTable(tables.Table):
    details = tables.TemplateColumn('<a href="works/{{record.category}}/{{record.id}}">Show details</a>', orderable=False)
    class Meta:
        model = Work
        template = 'django_tables2/bootstrap.html'
        fields = ('pk', 'category', 'title', 'addTime', 'average')
        empty_text = "There are no customers matching the search criteria..."