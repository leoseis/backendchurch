from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    AnnouncementViewSet,
    CategoryViewSet,
    CommentCreateView,
    SermonViewSet,
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