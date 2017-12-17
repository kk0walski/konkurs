from django import forms
from cuser.models import CUser
from .models import Uczestnik

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = CUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Uczestnik
        fields = ('birthday', 'place_of_birth', 'alias', 'phone_number', 'cellphone_number', 'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode')