from django.test import TestCase
import datetime
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from .forms import ProfileForm

# Create your tests here.
from cuser.models import CUser
from konkurs.models import Uczestnik, Picture

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
                        bio='dupa',
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
        form_data = {'birthday':'2005-01-20',
                'place_of_birth':'Wrocław',
                'phone_number':'+41 52 424 2424',
                'cellphone_number':'+41 52 424 2424',
                'nationality':'Poland',
                'biography':'costam',
                'country':'Poland',
                'city':'Kalisz',
                'street_line':'Hanki Sawickiej',
                'site':'www.karolkowalski.pl',
                'zipcode':'62500'}
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())