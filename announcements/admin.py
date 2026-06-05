from django.contrib import admin
from .models import Announcement, Category,Comment, Gallery, PrayerRequest, Sermon, Testimony
from .models import DailyDevotional

admin.site.register(DailyDevotional)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Sermon)

admin.site.register(PrayerRequest)
from .models import (
    Event,
    EventRegistration,

)

admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(EventRegistration)

admin.site.register(Testimony)

from .models import GivingAccount

@admin.register(GivingAccount)
class GivingAccountAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "bank_name",
        "account_number",
    )