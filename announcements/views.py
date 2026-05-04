from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny
from rest_framework import generics, permissions
from .models import Announcement, Category, Comment
from .serializers import AnnouncementSerializer, CategorySerializer, CommentSerializer


# 🔐 Custom Permission (BEST PRACTICE)
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # ✅ Anyone can READ
        if request.method in SAFE_METHODS:
            return True
        
        # 🔒 Only admin can WRITE
        return request.user and request.user.is_staff


# 📢 Announcements
class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all().order_by("-created_at")
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]   # ✅ BETTER THAN AllowAny


# 📂 Categories
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]   # ✅ Protect writes


# 💬 Comments (ONLY logged-in users)
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)