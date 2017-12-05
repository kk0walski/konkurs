from django import forms
from .models import Uczestnik


class UczestnikForm(forms.ModelForm):
    
    class Meta:
        model = Uczestnik
        fields = ('email', 'firstname', 'alias', 'lastname', 'birthday', 'place_of_birth', 'phone_number',
                  'cellphone_number', 'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode')
