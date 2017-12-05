from datetime import date
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))

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
    email = models.EmailField(primary_key=True, validators=[
                              validators.EmailValidator()])
    firstname = models.CharField(_('Firstname'), max_length=50, blank=False)
    lastname = models.CharField(_('Lastname'), max_length=50, blank=False)
    birthday = models.DateField(validators=[MinAgeValidator(18)])
    place_of_birth = models.CharField(
        _('Place Of Birth'), default='Kalisz', max_length=30, blank=False)
    alias = models.CharField(_('Alias'), max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    cellphone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    nationality = models.CharField(max_length=30, choices=NATIONALITY)
    biography = models.TextField()
    country = models.CharField(max_length=30, choices=NATIONALITY)
    city = models.CharField(_('City'), max_length=100, blank=True)
    street_line = models.CharField(_('Address'), max_length=100, blank=True)
    site = models.CharField(max_length=50)
    zipcode = models.CharField(_('ZIP code'), max_length=5, blank=True)

class Review(models.Model):
    author = models.ForeignKey(User, related_name='Autor', on_delete=models.DO_NOTHING)
    work = models.ForeignKey('Work',  on_delete=models.DO_NOTHING)    

class Work(models.Model):
    reviews = models.ManyToManyField(User, through=Review)
    autor = models.ForeignKey('Uczestnik', on_delete=models.CASCADE)
    
class Sculpture(Work):
    wymiary = models.CharField(max_length=30)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz1 = models.ImageField()
    obraz2 = models.ImageField()
    obraz3 = models.ImageField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50)
    year = models.IntegerField()

class Paint(Work):
    title = models.CharField(max_length=30)
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField()
    technika = models.CharField(max_length=20)
    year = models.IntegerField()

class VirtualArt(Work):
    title = models.CharField(max_length=30)
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz1 = models.ImageField()
    obraz2 = models.ImageField()
    obraz3 = models.ImageField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50)
    year = models.IntegerField()

class DigitalGraphic(Work):
    title = models.CharField(max_length=30)
    obraz = models.ImageField()
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    year = models.IntegerField()

class Picture(Work):
    title = models.CharField(max_length=30)
    wymiary = models.CharField(max_length=10)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField()
    technika = models.CharField(max_length=20)
    year = models.IntegerField()

class Video(Work):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=20)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField()
    year = models.IntegerField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50)

class Performence(Work):
    title = models.CharField(max_length=30)
    time = models.CharField(max_length=20)
    opis = models.TextField()
    cena = models.CharField(max_length=10)
    obraz = models.ImageField()
    year = models.IntegerField()
    video_url = models.URLField()
    video_password = models.CharField(max_length=50)

class LandArt(Work):
    title = models.CharField(max_length=30)
    obraz1 = models.ImageField()
    obraz2 = models.ImageField()
    obraz3 = models.ImageField()
    opis = models.TextField()

class UrbanArt(Work):
    title = models.CharField(max_length=30)
    obraz1 = models.ImageField()
    obraz2 = models.ImageField()
    obraz3 = models.ImageField()
    opis = models.TextField()