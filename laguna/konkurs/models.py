import os
from datetime import date, timedelta, datetime
from django.conf import settings
from django.core import validators
from django.core.validators import BaseValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))

def directory_path(instance, filename):
    return os.path.join(instance.autor.user.email, type(instance).__name__, filename)

@deconstructible
class MinAgeValidator(BaseValidator):
    compare = lambda self, a, b: calculate_age(a) < b
    message = _("Age must be at least %(limit_value)d.")
    code = 'min_age'

class Uczestnik(models.Model):
    NATIONALITY = (
        ("Afghanistan", 'Afganistan'),
        ("Albania", 'Albania'),
        ("Algeria", 'Algeria'),
        ("America", 'Ameryka'),
        ("Andorra", 'Andora'),
        ("Angola", 'Angola'),
        ("Anguilla", 'Anguilla'),
        ("Argentina", 'Argentyna'),
        ("Armenia", 'Armenia'),
        ("Australia", 'Australia'),
        ("Austria", 'Austria'),
        ("Azerbaijan", 'Azerbaijani'),
        ("the Bahamas", 'Bahamy'),
        ("Bahrain", 'Bahrain'),
        ("Bangladesh", 'Bangladesz'),
        ("Barbados", 'Barbados'),
        ("Barbudans", 'Barbudany'),
        ("Botswana", 'Botswana'),
        ("Belarus", 'Białoruś'),
        ("Belgium", 'Belgia'),
        ("Belize", 'Belize'),
        ("Benin", 'Benin'),
        ("Bhutan", 'Bhutan'),
        ("Bolivia", 'Boliwia'),
        ("Bosnia", 'Bośnia'),
        ("Brazylia", 'Brazylia'),
        ("Britain", 'Wielka Brytania'),
        ("Bruneia", 'Bruneia'),
        ("Bulgaria", 'Bułgaria'),
        ("Burkina Faso", 'Burkina Faso'),
        ("Burma", 'Birma'),
        ("Burgundia", 'Burgundia'),
        ("Cambodia", 'Kambodża'),
        ("Cameroon", 'Kamerun'),
        ("Canada", 'Kanada'),
        ("Cape Verde", 'Republika Zielonego Przylądka'),
        ("Central Africa", 'Centralna Afryka'),
        ("Chad", 'Czad'),
        ("Chile", 'Chile'),
        ("China", 'Chiny'),
        ("Colombia", 'Kolumbia'),
        ("Camorra", 'Camorra'),
        ("Democratic Republic of the Congo", 'Demokratyczna Republika Konga'),
        ("Costa Rica", 'Kostaryka'),
        ("Croatia", 'Chorwacja'),
        ("Cuba", 'Kuba'),
        ("Cyprus", 'Cypr'),
        ("Czechia", 'Czechy'),
        ("Denmark", 'Dania'),
        ("Djibouti", 'Dżibuti'),
        ("Dominica", 'Dominika'),
        ("Holland", 'Holandia'),
        ("East Timor", 'Wschodni Timor'),
        ("Ecuador", 'Ekwador'),
        ("Egypt", 'Egipt'),
        ("United Arab Emirates", 'Zjednoczone Emiraty Arabskie'),
        ("Equatorial Guinea", 'Ginea Równikowa'),
        ("Eritrea", 'Erytrea'),
        ("Estonia", 'Estonia'),
        ("Ethiopia", 'Etiopia'),
        ("Fiji", 'Fidżi'),
        ("Philippines", 'Filipiny'),
        ("Finn", 'Finy'),
        ("France", 'Francja'),
        ("Gabon", 'Gabon'),
        ("Gambia", 'Gambia'),
        ("Georgia", 'Gruzja'),
        ("Germany", 'Niemcy'),
        ("Ghana", 'Ghana'),
        ("Greece", 'Grecja'),
        ("Grenada", 'Grenada'),
        ("Guatemala", 'Guatemala'),
        ("Guinea-Bissau", 'Gwinea Bissau'),
        ("Guinea", 'Gwinea'),
        ("Guyana", 'Gujana'),
        ("Haiti", 'Haiti'),
        ("Herzegovina", 'Hercegowina'),
        ("Honduras", 'Honduras'),
        ("Hungary", 'Węgry'),
        ("Iceland", 'Islandia'),
        ("India", 'Indie'),
        ("Indonesia", 'Indonezja'),
        ("Iran", 'Iran'),
        ("Iraq", 'Irak'),
        ("Ireland", 'Irlandia'),
        ("Israel", 'Izrael'),
        ("Italy", 'Włochy'),
        ("Ivory Coast", 'Wybrzeże Kości Słoniowej'),
        ("Jamaica", 'Jamajka'),
        ("Japan", 'Japonia'),
        ("Jordan", 'Jordania'),
        ("Kazakhstan", 'Kazakhstan'),
        ("Kenya", 'Kenia'),
        ("Kittian and Nevisian", 'Kittan and Nevisian'),
        ("Kuwait", 'Kuwejt'),
        ("Kyrgyzstan", 'Kirgistan'),
        ("Lao", 'Laos'),
        ("Latvia", 'Łotwa'),
        ("Lebanon", 'Liban'),
        ("Liberia", 'Liberia'),
        ("Libya", 'Libia'),
        ("Liechtenstein", 'Liechtenstein'),
        ("Lithuania", 'Litwa'),
        ("Luxembourg", 'Luksemburg'),
        ("Macedonia", 'Macedonia'),
        ("Madagascar", 'Madagaskar'),
        ("Malawi", 'Malawi'),
        ("Malaysia", 'Malezja'),
        ("Maldives", 'Malediwy'),
        ("Malia", 'Malia'),
        ("Malaysia", 'Malezja'),
        ("the Marshall Islands", 'Wyspy Marshalla'),
        ("Mauritania", 'Mauretania'),
        ("Mexic", 'Meksyk'),
        ("Micronesia", 'Mikronezja'),
        ("Moldova", 'Mołdawia'),
        ("Monaco", 'Monako'),
        ("Mongolia", 'Mongolia'),
        ("Morocco", 'Maroko'),
        ("Lesotho", 'Lesotho'),
        ("Mozambique", 'Mozambik'),
        ("Namibia", 'Namibia'),
        ("Nauruan", 'Republika Nauru'),
        ("Nepal", 'Nepal'),
        ("New Zealand", 'Nowa Zelandia'),
        ("Nicaragua", 'Nikaragua'),
        ("Nigeria", 'Nigeria'),
        ("North Korea", 'Korea Północna'),
        ("Norway", 'Norwegia'),
        ("Oman", 'Oman'),
        ("Pakistan", 'Pakistan'),
        ("Palau", 'Palau'),
        ("Panama", 'Panama'),
        ("Papua New Guinea", 'Papua Nowa Gwinea'),
        ("Paraguay", 'Paragwaj'),
        ("Peru", 'Peru'),
        ("Poland", 'Polska'),
        ("Portugal", 'Portugalia'),
        ("Qatar", 'Katar'),
        ("Romania", 'Rumunia'),
        ("Russia", 'Rosja'),
        ("Rwanda", 'Rwanda'),
        ("Saint Lucia", 'Saint Lucia'),
        ("Salvador", 'Salwador'),
        ("Samoa", 'Samoa'),
        ("San Marino", 'San Marino'),
        ("Saudi Arabia", 'Arabia Saudyjska'),
        ("Scotland", 'Szkocja'),
        ("Senegal", 'Senegal'),
        ("Serbia", 'Serbia'),
        ("Seychelles", 'Seszele'),
        ("Sierra Leone", 'Sierra Leone'),
        ("Singapore", 'Singapur'),
        ("Slovakia", 'Słowacja'),
        ("Slovenia", 'Słowenia'),
        ("Solomon Island", 'Wyspa Salomona'),
        ("Somalia", 'Somalia'),
        ("South Africa", 'Połódniowa Afryka'),
        ("South Korea", 'Połódniowa Korea'),
        ("Spain", 'Hiszpania'),
        ("Sri Lanka", 'Sri Lanka'),
        ("Sudan", 'Sudan'),
        ("Surinam", 'Surinam'),
        ("Swaziland", 'Suazi'),
        ("Sweden", 'Szwecja'),
        ("Switzerland", 'Szwajcaria'),
        ("Syria", 'Syria'),
        ("Taiwan", 'Tajwan'),
        ("Tajikistan", 'Tadżykistan'),
        ("Tanzania", 'Tanzania'),
        ("Thailand", 'Tajlandia'),
        ("Togo", 'Togo'),
        ("Tonga", 'Tongo'),
        ("Tobago", 'Tobago'),
        ('Trinidad', 'Trynidad'),
        ("Tunisia", 'Tunezja'),
        ("Turkey", 'Turcja'),
        ("Tuvalu", 'Tuvalu'),
        ("Uganda", 'Uganda'),
        ("Ukraina", 'Ukraine'),
        ("Uruguay", 'Urugwaj'),
        ("Uzbekistan", 'Uzbekistan'),
        ("Venezuela", 'Wenezuela'),
        ("Vietnam", 'Wietnam'),
        ("Wales", 'Walia'),
        ("Yemen", 'Jemen'),
        ("Zambia", 'Zambia'),
        ("Zimbabwe", 'Zimbabwe')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    birthday = models.DateField(validators=[MinAgeValidator(18)], default = date.today)
    place_of_birth = models.CharField(
        _('Place Of Birth'), default='Kalisz', max_length=30, blank=False)
    alias = models.CharField(_('Alias'), max_length=50)
    phone_number = PhoneNumberField()
    cellphone_number = PhoneNumberField()
    nationality = models.CharField(max_length=30, choices=NATIONALITY)
    biography = models.TextField()
    country = models.CharField(max_length=30, choices=NATIONALITY)
    city = models.CharField(_('City'), max_length=100, blank=True)
    street_line = models.CharField(_('Address'), max_length=100, blank=True)
    site = models.CharField(max_length=50)
    zipcode = models.CharField(_('ZIP code'), max_length=5, blank=True)

class Work(models.Model):
    CATEGORY = (
        ('Sculpture', 'Rzeźba'),
        ('Paint', 'Obraz'),
        ('VirtualArt', 'SztukaWirtualna'),
        ('DigitalGraphics', 'GrafikaCyfrowa'),
        ('Picture', 'Zdjęcie'),
        ('Video', 'Video'),
        ('Performence', 'Występ'),
        ('LandArt', 'LandArt'),
        ('UrbanArt', 'UrbanArt')
    )
    category = models.CharField(max_length=30, choices=CATEGORY)
    title = models.CharField(max_length=30)
    autor = models.ForeignKey('Uczestnik', on_delete=models.CASCADE)
    addTime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

class Sculpture(Work):
    wymiary = models.CharField(max_length=30)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz1 = models.ImageField(upload_to=directory_path)
    obraz2 = models.ImageField(upload_to=directory_path)
    obraz3 = models.ImageField(upload_to=directory_path)
    video_url = models.URLField()
    video_password = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField()

class Paint(Work):
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField(upload_to=directory_path)
    technika = models.CharField(max_length=20)
    year = models.IntegerField()

class VirtualArt(Work):
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz1 = models.ImageField(upload_to=directory_path)
    obraz2 = models.ImageField(upload_to=directory_path)
    obraz3 = models.ImageField(upload_to=directory_path)
    video_url = models.URLField()
    video_password = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField()

class DigitalGraphic(Work):
    obraz = models.ImageField(upload_to=directory_path)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    year = models.IntegerField()

class Picture(Work):
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField(upload_to=directory_path)
    technika = models.CharField(max_length=20)
    year = models.IntegerField()

class Video(Work):
    time = models.DurationField(validators=[MaxValueValidator(timedelta(minutes=20), message="Za długi film")])
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField(upload_to=directory_path)
    year = models.IntegerField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50, null=True, blank=True)

class Performence(Work):
    time = models.DurationField(validators=[MaxValueValidator(timedelta(minutes=20), message="Za długi film")])
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField(upload_to=directory_path)
    year = models.IntegerField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50)

class LandArt(Work):
    obraz1 = models.ImageField(upload_to=directory_path)
    obraz2 = models.ImageField(upload_to=directory_path)
    obraz3 = models.ImageField(upload_to=directory_path)
    opis = models.TextField()

class UrbanArt(Work):
    obraz1 = models.ImageField(upload_to=directory_path)
    obraz2 = models.ImageField(upload_to=directory_path)
    obraz3 = models.ImageField(upload_to=directory_path)
    opis = models.TextField()