from django import forms
from cuser.models import CUser
from .models import Uczestnik, Sculpture, Paint, Picture, VirtualArt, Video, Performence, LandArt, UrbanArt, DigitalGraphic
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Powtórz hasło', widget=forms.PasswordInput)

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
        fields = ('birthday', 'place_of_birth', 'alias', 'phone_number', 'cellphone_number',
                  'nationality', 'biography', 'country', 'city', 'street_line', 'site', 'zipcode')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': PhoneNumberPrefixWidget(),
            'cellphone_number': PhoneNumberPrefixWidget(),
        }


class SculptureForm(forms.ModelForm):
    class Meta:
        model = Sculpture
        fields = ('title', 'wymiary', 'opis', 'cena', 'obraz1',
                  'obraz2', 'obraz3', 'video_url', 'video_password', 'year')


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


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'time', 'opis', 'cena', 'obraz',
                  'year', 'video_url', 'video_password')


class PerformenceForm(forms.ModelForm):
    class Meta:
        model = Performence
        fields = ('title', 'time', 'opis', 'cena', 'obraz',
                  'year', 'video_url', 'video_password')


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
