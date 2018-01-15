import django_filters
from .models import Work

class WorkListFilter(django_filters.FilterSet):
    """Filtr umożliwiający filtrowanie po kategorii, tytule, czasu dodania oraz średniej ocenie"""
    class Meta:
        model = Work
        fields = {
            'category' : ['exact'],
            'title' : ['contains'],
            'addTime' : ['month', 'day', 'year'],
            'average' : ['exact']
        }