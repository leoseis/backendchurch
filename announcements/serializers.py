from rest_framework import serializers
from .models import Announcement, Category, Comment


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