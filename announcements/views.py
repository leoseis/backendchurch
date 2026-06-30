from rest_framework.viewsets import ModelViewSet
from .models import BibleReadingPlan, Sermon
from .serializers import BibleReadingPlanSerializer, GallerySerializer, GivingAccountSerializer, LiveServiceSerializer, SermonSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import generics, permissions, viewsets
from .models import Announcement, Category, Comment, DailyDevotional
from .models import DailyDevotional
from .serializers import DailyDevotionalSerializer
from rest_framework.permissions import AllowAny
from .models import Testimony, ChurchBranch
from .serializers import TestimonySerializer, ChurchBranchSerializer
from .models import ServiceSchedule

from .serializers import (
    ServiceScheduleSerializer
)
from .serializers import (
    AnnouncementSerializer,
    CategorySerializer,
    CommentSerializer,
    DailyDevotionalSerializer
)
from .models import (
    Event,
    EventRegistration,
    GivingAccount,
    Gallery,
    LiveStream,
    LiveService,
)

from .serializers import (
    EventSerializer,
    EventRegistrationSerializer,
    LiveStreamSerializer,
)


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PrayerRequest
from .serializers import PrayerRequestSerializer

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

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


class SermonViewSet(ModelViewSet):

    queryset = Sermon.objects.all().order_by(
        "-created_at"
    )

    serializer_class = SermonSerializer

    permission_classes = [AllowAny]



class PrayerRequestViewSet(
    ModelViewSet
):

    queryset = PrayerRequest.objects.all().order_by(
        "-created_at"
    )

    serializer_class = PrayerRequestSerializer

    permission_classes = [AllowAny]




class EventViewSet(ModelViewSet):
    queryset = Event.objects.all().order_by("event_date")

    serializer_class = EventSerializer


class EventRegistrationViewSet(ModelViewSet):
    queryset = EventRegistration.objects.all()

    serializer_class = EventRegistrationSerializer



class DailyDevotionalViewSet(
    ModelViewSet
):

    queryset = DailyDevotional.objects.all().order_by(
        "-devotional_date"
    )

    serializer_class = (
        DailyDevotionalSerializer
    )

    permission_classes = [AllowAny]



class GivingAccountViewSet(ModelViewSet):
    queryset = GivingAccount.objects.all()
    serializer_class = GivingAccountSerializer
    permission_classes = [IsAdminOrReadOnly]



class TestimonyViewSet(
    ModelViewSet
):

    queryset = Testimony.objects.all().order_by(
        "-created_at"
    )

    serializer_class = (
        TestimonySerializer
    )

    permission_classes = [AllowAny]





class GalleryViewSet(
    viewsets.ModelViewSet
):
    queryset = Gallery.objects.all()

    serializer_class = GallerySerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]




class LiveStreamViewSet(
    viewsets.ModelViewSet
):
    queryset = LiveStream.objects.all()

    serializer_class = (
        LiveStreamSerializer
    )

    permission_classes = [
        IsAdminOrReadOnly
    ]



class LiveServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiveService.objects.filter(is_live=True)
    serializer_class = LiveServiceSerializer



class BibleReadingPlanViewSet(
    viewsets.ModelViewSet
):
    queryset = (
    BibleReadingPlan.objects.all()
        .order_by("reading_date")
    )

    serializer_class = (
    BibleReadingPlanSerializer
    )

    permission_classes = [AllowAny]



class ServiceScheduleViewSet(
    viewsets.ModelViewSet
):
    queryset = (
        ServiceSchedule.objects.all()
    )

    serializer_class = (
        ServiceScheduleSerializer
    )

class ChurchBranchViewSet(
    viewsets.ModelViewSet
):
    queryset = ChurchBranch.objects.all()

    serializer_class = (
        ChurchBranchSerializer
    )





