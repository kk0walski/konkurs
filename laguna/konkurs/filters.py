import django_filters
from .models import Work

class WorkListFilter(django_filters.FilterSet):
    class Meta:
        model = Work
        fields = ['category', 'title', 'addTime']