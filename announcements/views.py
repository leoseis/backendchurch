from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics, permissions
from .models import Announcement, Category, Comment
from .serializers import (
    AnnouncementSerializer,
    CategorySerializer,
    CommentSerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# =========================
# CUSTOM PERMISSION
# =========================
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        # Anyone can READ
        if request.method in SAFE_METHODS:
            return True

        # Only admin can WRITE
        return request.user and request.user.is_staff


# =========================
# ANNOUNCEMENTS
# =========================
class AnnouncementViewSet(ModelViewSet):

    queryset = Announcement.objects.all().order_by("-created_at")

    serializer_class = AnnouncementSerializer

    permission_classes = [IsAdminOrReadOnly]


    def get_queryset(self):

        queryset = Announcement.objects.all().order_by("-created_at")

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(category__name=category)

        return queryset
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminOrReadOnly]

    # ✅ LIKE SYSTEM
    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def like(self, request, pk=None):

        announcement = self.get_object()

        # Toggle Like
        if request.user in announcement.likes.all():
            announcement.likes.remove(request.user)
            liked = False
        else:
            announcement.likes.add(request.user)
            liked = True

        announcement.refresh_from_db()

        return Response({
            "liked": liked,
            "likes_count": announcement.likes.count(),
        })


# =========================
# CATEGORIES
# =========================
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


# =========================
# COMMENTS
# =========================
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)