from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AnnouncementViewSet,
    CategoryViewSet,
    CommentCreateView,
)

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path(
        'comments/create/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),
]