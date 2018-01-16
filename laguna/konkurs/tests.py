import os, io
import laguna.settings as settings
from django.test import TestCase
import datetime
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from .forms import ProfileForm, UserForm, VideoForm
from phonenumber_field.phonenumber  import PhoneNumber

# Create your tests here.
from cuser.models import CUser
from konkurs.models import Uczestnik, Picture
from django.db.models.fields.files import ImageFieldFile

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
            email='sekretarz@gmail.com'
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
        path = os.path.join(settings.MEDIA_ROOT, 'jan.nowak@gmail.com\Picture\IMG_20171209_195254_processed.jpg')
                file = open(path, "rb")
        obraz = ImageFieldFile(file = )
        obraz.file
        file_dict = {'file':SimpleUploadedFile(file.name, file.read()).}
        data = {
                "title":"title",
                "time":"15:00",
                "opis":"opis",
                "cena":"0 zł",
                "obraz": "jan.nowak@gmail.com/Picture/IMG_20171209_195254_processed.jpg",
                'year':2010,
                'video_url':"http://www.youtube.com",
                'video_password': "password"
            }
        form = VideoForm(data=data, files=file_dict)
        print(file_dict)
        form.is_valid()
        file.close()
        print(form.errors)