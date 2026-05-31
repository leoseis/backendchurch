from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    AnnouncementViewSet,
    CategoryViewSet,
    CommentCreateView,
    DailyDevotionalViewSet,
    SermonViewSet,
    PrayerRequestViewSet,
    EventViewSet,
    EventRegistrationViewSet,
)

router = DefaultRouter()

# ANNOUNCEMENTS
router.register(
    r'announcements',
    AnnouncementViewSet
)

# CATEGORIES
router.register(
    r'categories',
    CategoryViewSet
)

# SERMONS
router.register(
    r'sermons',
    SermonViewSet
)

# PRAYERS
router.register(
    r'prayers',
    PrayerRequestViewSet
)

# EVENTS
router.register(
    r'events',
    EventViewSet
)

# EVENT REGISTRATIONS
router.register(
    r'event-registrations',
    EventRegistrationViewSet
)

# DEVOTIONALS
router.register(
    r'devotionals',
    DailyDevotionalViewSet
)

urlpatterns = [

    path(
        '',
        include(router.urls)
    ),

    path(
        'comments/create/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),
]