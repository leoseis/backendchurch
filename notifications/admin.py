from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DeviceToken


@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "device_name",
        "token",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "device_name",
        "token",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)