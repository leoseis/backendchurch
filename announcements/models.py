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