from django import forms
from django.contrib.auth.forms import AuthenticationForm
from cuser.models import CUser
from .models import Uczestnik, Sculpture, Paint, Picture, VirtualArt, Video, Performence, LandArt, UrbanArt, DigitalGraphic
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return super().clean()

class UserForm(forms.ModelForm):
    """Formularz rejestracji użytkownika"""
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = CUser
        fields = ('email', 'first_name', 'last_name')
    """Sprawdzenie czy hasła się zgadzają"""
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = CUser.objects.get(email=email.lower())
        except CUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

"""Formularz edycji użytkownika"""
class UserEditForm(forms.ModelForm):
    class Meta:
        model = CUser
        fields = ('email', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Uczestnik
        fields = ('birthday', 'place_of_birth', 'alias', 'phone_number', 'cellphone_number',
                  'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class SculptureForm(forms.ModelForm):
    class Meta:
        model = Sculpture
        fields = ('title', 'wymiary', 'opis', 'cena', 'obraz1',
                  'obraz2', 'obraz3', 'video_url', 'video_password', 'year')
        widgets = {
                    'video_password' : forms.PasswordInput(),
        }


class PaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = ('title', 'wymiary', 'opis', 'cena',
                  'obraz', 'technika', 'year')


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('title', 'wymiary', 'opis', 'cena',
                  'obraz', 'technika', 'year')


class VirtualArtForm(forms.ModelForm):
    class Meta:
        model = VirtualArt
        fields = ('title', 'wymiary', 'opis', 'cena', 'obraz1',
                  'obraz2', 'obraz3', 'video_url', 'video_password', 'year')
        widgets = {
                    'video_password' : forms.PasswordInput(),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'time', 'opis', 'cena', 'obraz',
                  'year', 'video_url', 'video_password')
        widgets = {
            'time' : forms.DateInput(attrs={'type': 'time'}),
            'video_password' : forms.PasswordInput(),
        }


class PerformenceForm(forms.ModelForm):
    class Meta:
        model = Performence
        fields = ('title', 'time', 'opis', 'cena', 'obraz',
                  'year', 'video_url', 'video_password')
        widgets = {
            'time' : forms.DateInput(attrs={'type': 'time'}),
            'video_password' : forms.PasswordInput(),
        }


class LandArtForm(forms.ModelForm):
    class Meta:
        model = LandArt
        fields = ('title', 'obraz1', 'obraz2', 'obraz3', 'opis')


class UrbanArtForm(forms.ModelForm):
    class Meta:
        model = UrbanArt
        fields = ('title', 'obraz1', 'obraz2', 'obraz3', 'opis')


class DigitalGraphicsForm(forms.ModelForm):
    class Meta:
        model = DigitalGraphic
        fields = ('title', 'obraz', 'opis', 'cena', 'year')
