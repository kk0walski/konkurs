from django.forms import ModelForm
from .models import Uczestnik


class UczestnikForm(ModelForm):
    class Meta:
        model = Uczestnik
        fields = ['email', 'firstname', 'alias', 'lastname', 'birthday', 'place_of_birth', 'phone_number',
                  'cellphone_number', 'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode']
