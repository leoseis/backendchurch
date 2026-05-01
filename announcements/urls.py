from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, AnnouncementListCreateView, AnnouncementDetailView,CommentCreateView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('announcements/', AnnouncementListCreateView.as_view()),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view()),
     path('comments/', CommentCreateView.as_view(), name='create-comment'),
]

# 🔥 THIS LINE IS VERY IMPORTANT
urlpatterns += router.urls