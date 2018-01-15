Models
------

Uczestnik
===============

This are fields of model Uczestnik::

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    """Wiek uczestnika musi być co najmniej 18"""
    birthday = models.DateField(validators=[MinAgeValidator(18)], default = date.today)
    place_of_birth = models.CharField(
        _('Place Of Birth'), default='Kalisz', max_length=30, blank=False)
    alias = models.CharField(_('Alias'), max_length=50, null=True)
    phone_number = PhoneNumberField()
    cellphone_number = PhoneNumberField()
    nationality = models.CharField(max_length=30, choices=NATIONALITY)
    biography = models.TextField()
    country = models.CharField(max_length=30, choices=NATIONALITY)
    city = models.CharField(_('City'), max_length=100)
    street_line = models.CharField(_('Address'), max_length=100)
    site = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(_('ZIP code'), max_length=5)

    def __str__(self):
        return '{}'.format(self.id)
