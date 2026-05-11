from django.contrib import admin
from .models import Announcement, Category,Comment


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")


admin.site.register(Category)
admin.site.register(Comment)