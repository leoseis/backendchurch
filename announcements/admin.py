from django.contrib import admin
from .models import Announcement, Category


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "is_active")

    # 🔥 FORCE FIELDS TO SHOW
    fields = (
        "title",
        "body",
        "category",        # ✅ THIS IS THE IMPORTANT ONE
        "author",
        "image",
        "is_active",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")




    