from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        return super().setUp()

    def test_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
