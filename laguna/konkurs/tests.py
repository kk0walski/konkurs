import os, base64, io
from PIL import Image
from django.core.files import File
import laguna.settings as settings
from django.test import TestCase
import datetime
from django.urls import reverse
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from .forms import ProfileForm, UserForm, VideoForm
from phonenumber_field.phonenumber  import PhoneNumber
from django.test import Client

# Create your tests here.
from cuser.models import CUser
from konkurs.models import Uczestnik, Picture
from django.core.files.uploadedfile import InMemoryUploadedFile

class CurserTestModel(TestCase):
    """
    Class to test the model
    Curser
    """
    @staticmethod
    def create_uczestnik(uzytkownik, 
                        age=datetime.date(1999,1,20),
                        cellphone='+41 52 424 2424',
                        phone='+41 52 424 2424',
                        nation='Poland',
                        bio='Jakaś biografia',
                        coun='Poland',
                        cit='Wrocław',
                        street='Kościuszki 175A',
                        zip='62800',):
        return Uczestnik.objects.create(user=uzytkownik,
                                        birthday=age,
                                        phone_number=phone,
                                        cellphone_number=cellphone,
                                        nationality=nation,
                                        biography=bio,
                                        country=coun,
                                        city=cit,
                                        street_line=street,
                                        zipcode=zip
    )

    def setUp(self):
        """
        Set up all the tests
        """
        self.cuser = mommy.make(
            CUser,
            email='konrad.staszewski@gmail.com'
            )
        self.admin = mommy.make(
            CUser,
            email='karol.kowalski95@gmail.com'
        )
        self.sekretarz = mommy.make(
            CUser,
            email='sekretarz@gmail.com',
            password="password"
        )
        self.uczestnik = self.create_uczestnik(uzytkownik=self.cuser)
    
    def test_createUczestnik(self):
        self.assertEqual(self.uczestnik.user, self.cuser)
        self.assertEqual(Uczestnik.objects.count(), 1)

    def test_validation(self):
        form_data = {
                "birthday": "2005-01-26",
                "place_of_birth": "Kalisz",
                "alias": "ryzer",
                "phone_number": str(PhoneNumber.from_string("+48 12 345 6789")),
                "cellphone_number": str(PhoneNumber.from_string("+48 12 345 6789")),
                "nationality": "Poland",
                "biography": "dadadsdsdsdsad",
                "country": "Poland",
                "city": "Pakistan",
                "street_line": "Ulica powsta\u0144c\u00f3w",
                "site": "http://www.google.pl",
                "zipcode": "52800"
                }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'birthday': ['Age must be at least 18.']})
        form2 = ProfileForm(
            {
                "birthday": "1995-01-26",
                "place_of_birth": "Kalisz",
                "alias": "ryzer",
                "phone_number": str(PhoneNumber.from_string("+48 12 345 6789")),
                "cellphone_number": str(PhoneNumber.from_string("+48 12 345 6789")),
                "nationality": "Poland",
                "biography": "dadadsdsdsdsad",
                "country": "Poland",
                "city": "Pakistan",
                "street_line": "Ulica powsta\u0144c\u00f3w",
                "site": "http://www.google.pl",
                "zipcode": "52800"
                }
        )
        self.assertTrue(form2.is_valid())

    def test_userForm(self):
        form = UserForm(
            {
                "email":"example@gmail.com",
                "password":"password",
                "password2":"password2"
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2':['Hasła nie są identyczne']})
        form2 = UserForm(
            {
                "email":"example@gmail.com",
                "password":"password",
                "password2":"password"
            }
        )
        self.assertTrue(form2.is_valid())


    def test_time(self):
        path = os.path.join(settings.MEDIA_ROOT, r'jan.nowak@gmail.com\Picture\fotoshop.png')
        image = Image.open(path)
        TEST_IMAGE = image.tobytes()
        upload = InMemoryUploadedFile(
            io.BytesIO(TEST_IMAGE),
            field_name='fotoshop',
            name='fotoshop.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8'
        )
        data = {
                "title":"title",
                "time":"22:00",
                "opis":"opis",
                "cena":"0 zł",
                "obraz": upload,
                'year':2010,
                'video_url':"http://www.youtube.com",
                'video_password': "password"
            }
        form = VideoForm(data=data, files={'obraz':upload})
        form.is_valid()
        self.assertEqual(form.errors, {"obraz" : ['Upload a valid image. The file you uploaded was either not an image or a corrupted image.'], "time" : ["Za długi film"]})

    def you_must_login(self):
        c = Client()
        response = c.get(reverse('ListOfWorks'))
        self.assertEqual(response, '<HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/accounts/login/?next=/accounts/profile/worksToReview">')