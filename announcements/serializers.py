from rest_framework import serializers
from .models import Announcement, Category, Comment, DailyDevotional, GivingAccount, LiveStream, PrayerRequest, Sermon, Testimony, Gallery
from .models import (
    Event,
    EventRegistration,
)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = "__all__"

    def get_likes_count(self, obj):
        return obj.likes.count()
    



class SermonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sermon
        fields = "__all__"



class PrayerRequestSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = PrayerRequest
        fields = "__all__"



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = "__all__"




class DailyDevotionalSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DailyDevotional
        fields = "__all__"



class GivingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GivingAccount
        fields = "__all__"



class TestimonySerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Testimony
        fields = "__all__"



class GallerySerializer(
    serializers.ModelSerializer
):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery

        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get(
            "request"
        )

        if obj.image:
            return request.build_absolute_uri(
                obj.image.url
            )

        return None
    


class LiveStreamSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = LiveStream
        fields = "__all__"  