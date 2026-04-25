from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

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
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title