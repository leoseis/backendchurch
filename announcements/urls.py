from django.urls import path
from .views import AnnouncementListCreateView, AnnouncementDetailView

urlpatterns = [
    path('', AnnouncementListCreateView.as_view()),
    path('<int:pk>/', AnnouncementDetailView.as_view()),
]