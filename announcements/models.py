from django.db import models
from django.db.models.functions import Lower
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_category_name_case_insensitive'
            )
        ]


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # ✅ THIS IS THE CORRECT FIELD
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="announcements/", blank=True, null=True)


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    announcement = models.ForeignKey(
        'Announcement',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.content[:20]}"