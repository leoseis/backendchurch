from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(required=False)
    class Meta:
        model = Announcement
        fields = '__all__'