from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny
from rest_framework import generics, permissions
from .models import Announcement, Category, Comment
from .serializers import AnnouncementSerializer, CategorySerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes




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


@action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
def like(self, request, pk=None):
    announcement = self.get_object()

    if announcement.likes.filter(id=request.user.id).exists():
        announcement.likes.remove(request.user)
        liked = False
    else:
        announcement.likes.add(request.user)
        liked = True

    return Response({
        "liked": liked,
        "likes_count": announcement.likes.count()
    })

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





@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_announcement(request, pk):
    try:
        announcement = Announcement.objects.get(pk=pk)

        if request.user in announcement.likes.all():
            announcement.likes.remove(request.user)
            liked = False
        else:
            announcement.likes.add(request.user)
            liked = True

        return Response({
            "liked": liked,
            "likes_count": announcement.likes.count()
        })

    except Announcement.DoesNotExist:
        return Response(
            {"error": "Announcement not found"},
            status=404
        )