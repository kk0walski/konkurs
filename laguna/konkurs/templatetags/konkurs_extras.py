from django import template
from konkurs.models import Uczestnik

register = template.Library()

@register.filter
def user_is_uczestnik(user):
    return Uczestnik.objects.filter(user_id=user.pk).exists()