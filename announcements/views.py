from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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