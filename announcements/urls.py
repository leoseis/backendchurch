from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, CategoryViewSet, CommentCreateView

router = DefaultRouter()
router.register('announcements', AnnouncementViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentCreateView.as_view()),
]