from django.db import models
from django.conf import settings


# =========================
# CATEGORY
# =========================
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# =========================
# ANNOUNCEMENT
# =========================
class Announcement(models.Model):
    title = models.CharField(max_length=255)

    body = models.TextField()

    image = models.ImageField(
        upload_to="announcements/",
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_announcements",
        blank=True,
    )

    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title


# =========================
# COMMENT
# =========================
class Comment(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.author} - {self.announcement.title}"
    




class Sermon(models.Model):
    title = models.CharField(max_length=255)

    pastor = models.CharField(
        max_length=255
    )

    thumbnail = models.ImageField(
        upload_to="sermons/"
    )

    youtube_link = models.URLField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    

class PrayerRequest(models.Model):

    name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    request = models.TextField()

    is_anonymous = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        if self.is_anonymous:
            return "Anonymous Prayer"

        return self.name or "Prayer Request"
    



class Event(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    event_date = models.DateTimeField()

    venue = models.CharField(max_length=255)

    banner = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    department = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"
    

class DailyDevotional(models.Model):
    title = models.CharField(max_length=255)

    bible_verse = models.CharField(
        max_length=255
    )

    scripture_text = models.TextField()

    message = models.TextField()

    prayer = models.TextField()

    devotional_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title



class GivingAccount(models.Model):
    title = models.CharField(max_length=100)

    bank_name = models.CharField(max_length=100)

    account_name = models.CharField(max_length=200)

    account_number = models.CharField(max_length=30)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



class Testimony(models.Model):

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    author = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    



class Gallery(models.Model):
    title = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to="gallery/"
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title




class LiveStream(models.Model):
    title = models.CharField(max_length=255)

    youtube_url = models.URLField()

    is_live = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title