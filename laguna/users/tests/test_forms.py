from django.test import TestCase

from users.forms import UserForm


class AddUserForm(TestCase):
    def test_html(self):
        form = UserForm()
        self.assertFalse(form.is_valid())
        self.assertInHTML(
            '<input type="email" name="email" maxlength="254" required id="id_email">',
            str(form),
        )
        self.assertInHTML(
            '<input type="email" name="email" maxlength="254" required id="id_email">',
            str(form),
        )
        self.assertInHTML(
            '<input type="text" name="username" maxlength="150" required id="id_username">',
            str(form),
        )
        self.assertInHTML(
            '<input type="text" name="first_name" maxlength="150" id="id_first_name">',
            str(form),
        )
        self.assertInHTML(
            '<input type="text" name="last_name" maxlength="150" id="id_last_name">',
            str(form),
        )

    def test_empty_form(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['birthday'], ['This field is required.'])
        self.assertEqual(form.errors['nationality'], ['This field is required.'])
        self.assertEqual(form.errors['place_of_birth'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])