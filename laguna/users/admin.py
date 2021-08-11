from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Address, Participant


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = ("email", "is_staff", "is_active", "groups")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser, CustomUserAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    model = Participant
    list_display = ("user", "nationality" "birthday")
    list_filter = ("user", "nationality", "birthday")
    fieldsets = (
        (_("Contact info"), {"fields": ("user", "phone_number", "cellphone_number")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "birthday",
                    "site",
                    "nationality",
                )
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("user", "nationality")


admin.site.register(Participant, ParticipantAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_filter = ("user", "country", "city", "zip_code")
    list_display = ("fullAddress", "zip_code", "city", "country")
    fieldsets = (
        (_("Basic info"), {"fields": ("user", "fullAddress", "country", "city")}),
        (
            _("Address info"),
            {
                "fields": (
                    "address1",
                    "address2",
                    "zip_code",
                )
            },
        ),
    )


admin.site.register(Address, AddressAdmin)
