from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.index_url = reverse("index")
        return super().setUp()

    def test_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")