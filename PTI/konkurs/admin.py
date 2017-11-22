from django.contrib import admin

# Register your models here.
from system.models import Author, Competition, Registration

class AuthorAdmin(admin.ModelAdmin):
    pass

class CompetitionAdmin(admin.ModelAdmin):
    pass

class RegistrationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Registration, RegistrationAdmin)