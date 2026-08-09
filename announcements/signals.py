from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Announcement
from notifications.services import send_push_notification


@receiver(post_save, sender=Announcement)
def announcement_created(sender, instance, created, **kwargs):
    if created:
        send_push_notification(
            title="📢 New Announcement",
            body=instance.title,
            data={
                "announcement_id": instance.id,
            },
        )