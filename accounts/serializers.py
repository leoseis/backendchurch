from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_picture",
        ]

    def update(self, instance, validated_data):
     instance.first_name = validated_data.get(
        "first_name",
        instance.first_name,
    )

     instance.last_name = validated_data.get(
        "last_name",
        instance.last_name,
    )

     instance.email = validated_data.get(
        "email",
        instance.email,
    )

     instance.save()

     return instance


        