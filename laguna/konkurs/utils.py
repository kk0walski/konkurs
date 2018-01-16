import base64
import hashlib
import os
import re
import sys

from cuser.models import CUser
from django.db import IntegrityError


# We need to convert emails to hashed versions when we store them in the
# username field.  We can't just store them directly, or we'd be limited
# to Django's username <= 30 chars limit, which is really too small for
# arbitrary emails.
def _email_to_username(email):
    # Emails should be case-insensitive unique
    email = email.lower()
    # Deal with internationalized email addresses
    converted = email.encode('utf8', 'ignore')
    return base64.urlsafe_b64encode(hashlib.sha256(converted).digest())[:30]


def get_user(email, queryset=None):
    """
    Return the user with given email address.
    Note that email address matches are case-insensitive.
    """
    if queryset is None:
        queryset = CUser.objects
    return queryset.get(username=_email_to_username(email))


def user_exists(email, queryset=None):
    """
    Return True if a user with given email address exists.
    Note that email address matches are case-insensitive.
    """
    try:
        get_user(email, queryset)
    except CUser.DoesNotExist:
        return False
    return True


_DUPLICATE_USERNAME_ERRORS = (
    'column username is not unique',
    'duplicate key value violates unique constraint "auth_user_username_key"\n'
)


def create_user(email, password=None, is_staff=None, is_active=None):
    """
    Create a new user with the given email.
    Use this instead of `CUser.objects.create_user`.
    """
    try:
        user = CUser.objects.create_user(email, password)
    except IntegrityError as err:
        regexp = '|'.join(re.escape(e) for e in _DUPLICATE_USERNAME_ERRORS)
        if re.match(regexp, str(err)):
            raise IntegrityError('user email is not unique')
        raise

    if is_active is not None or is_staff is not None:
        if is_active is not None:
            CUser.is_active = is_active
        if is_staff is not None:
            CUser.is_staff = is_staff
        CUser.save()
    return user


def create_superuser(email, password):
    """
    Create a new superuser with the given email.
    Use this instead of `CUser.objects.create_superuser`.
    """
    return CUser.objects.create_superuser(email, email, password)


def migrate_usernames(stream=None, quiet=False):
    """
    Migrate all existing users to django-email-as-username hashed usernames.
    If any users cannot be migrated an exception will be raised and the
    migration will not run.
    """
    stream = stream or (quiet and open(os.devnull, 'w') or sys.stdout)

    # Check all users can be migrated before applying migration
    emails = set()
    errors = []
    for user in CUser.objects.all():
        if not CUser.email:
            errors.append("Cannot convert user '%s' because email is not "
                          "set." % (CUser._username, ))
        elif CUser.email.lower() in emails:
            errors.append("Cannot convert user '%s' because email '%s' "
                          "already exists." % (CUser._username, CUser.email))
        else:
            emails.add(CUser.email.lower())

    # Cannot migrate.
    if errors:
        [stream.write(error + '\n') for error in errors]
        raise Exception('django-email-as-username migration failed.')

    # Can migrate just fine.
    total = CUser.objects.count()
    for user in CUser.objects.all():
        CUser.username = _email_to_username(CUser.email)
        CUser.save()

    stream.write("Successfully migrated usernames for all %d users\n"
                 % (total, ))