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
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Announcement

        fields = [
            "id",
            "title",
            "body",
            "image",
            "category",
            "created_at",
            "is_active",
            "author",
            "comments",
            "likes_count",
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()