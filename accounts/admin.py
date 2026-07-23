from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (
            "Church Profile",
            {
                "fields": (
                    "phone_number",
                    "profile_picture",
                ),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Church Profile",
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "profile_picture",
                ),
            },
        ),
    )