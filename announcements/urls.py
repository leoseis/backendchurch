from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    AnnouncementViewSet,
    BibleReadingPlanViewSet,
    CategoryViewSet,
    CommentCreateView,
    DailyDevotionalViewSet,
    GalleryViewSet,
    GivingAccountViewSet,
    LiveStreamViewSet,
    SermonViewSet,
    PrayerRequestViewSet,
    EventViewSet,
    EventRegistrationViewSet,
    TestimonyViewSet,
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
router.register(
    r"reading-plans",
    BibleReadingPlanViewSet
)

router.register(
    r"gallery",
    GalleryViewSet
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
router.register(
    r"testimonies",
    TestimonyViewSet
)
router.register(
    r"giving",
    GivingAccountViewSet
)

router.register(
    r"livestreams",
    LiveStreamViewSet
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

