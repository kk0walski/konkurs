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
    list_display = ("user_email", "nationality", "user_first_name", "user_last_name")
    list_filter = ("user", "nationality")
    fieldsets = (
        (None, {"fields": ("user", "phone_number", "cellphone_number")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "user_username",
                    "user_first_name",
                    "user_last_name",
                    "birthday",
                    "site",
                    "nationality",
                )
            },
        ),
        (_("Important dates"), {"fields": ("user_last_login", "user_date_joined")}),
    )
    search_fields = ("user", "user_first_name", "user_last_name")
    ordering = ("user", "nationality")


    def user_username(self, obj):
        return obj.user.username

    def user_email(self, obj):
        return str(obj.user.email)

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

    def user_last_login(self, obj):
        return obj.user.last_login

    def user_date_joined(self, obj):
        return obj.user.date_joined

admin.site.register(Participant, ParticipantAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "fullAddress",
        "zip_code",
        "city",
    )


admin.site.register(Address, AddressAdmin)
