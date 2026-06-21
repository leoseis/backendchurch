from django.contrib import admin
from .models import Announcement, BibleReadingPlan, Category, ChurchBranch,Comment, Gallery, LiveStream, PrayerRequest, Sermon, Testimony
from .models import DailyDevotional
from .models import ServiceSchedule



@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")



admin.site.register(PrayerRequest)
from .models import (
    Event,
    EventRegistration,

)

admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(EventRegistration)
admin.site.register(BibleReadingPlan)
admin.site.register( ServiceSchedule)
admin.site.register(LiveStream)
admin.site.register(Testimony)
admin.site.register(DailyDevotional)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Sermon)
admin.site.register(ChurchBranch)

from .models import GivingAccount

@admin.register(GivingAccount)
class GivingAccountAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "bank_name",
        "account_number",
    )