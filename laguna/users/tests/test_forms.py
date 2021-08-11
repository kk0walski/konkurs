from django.test import TestCase

from users.forms import UserForm


class AddUserForm(TestCase):
    def test_html(self):
        form = UserForm()
        self.assertFalse(form.is_valid())
        #print(str(form))
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