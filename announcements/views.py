from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly  
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer

class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAdminOrReadOnly]





class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS (read-only)
        if request.method in SAFE_METHODS:
            return True
        
        # Only admin (staff) can modify
        return request.user and request.user.is_staff
    


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]   # 👈 THIS is the key lin




class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer