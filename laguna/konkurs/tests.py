from django.test import TestCase

from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Create your tests here.
from cuser.models import CUser

class CurserTestModel(TestCase):
    """
    Class to test the model
    Curser
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.curser = mommy.make(CUser)