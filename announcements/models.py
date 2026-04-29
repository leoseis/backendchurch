from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('youth', 'Youth'),
        ('women', 'Women'),
        ('men', 'Men'),
        ('choir', 'Choir'),
    ]

    title = models.CharField(max_length=255)
    body = models.TextField()

    # ✅ FIXED CATEGORY (CHOICES)
    category_type = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='general'
    )

    # ✅ DYNAMIC CATEGORY (OPTIONAL)
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='announcements/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title