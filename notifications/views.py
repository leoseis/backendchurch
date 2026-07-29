from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DeviceToken
from .serializers import DeviceTokenSerializer


class RegisterDeviceTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DeviceTokenSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data["token"]
            device_name = serializer.validated_data.get("device_name", "")

            DeviceToken.objects.update_or_create(
                token=token,
                defaults={
                    "user": request.user,
                    "device_name": device_name,
                },
            )

            return Response(
                {"message": "Device token registered successfully."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
