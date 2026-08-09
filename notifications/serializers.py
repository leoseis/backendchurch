from rest_framework import serializers
from .models import DeviceToken


from rest_framework import serializers
from .models import DeviceToken


class DeviceTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(validators=[])

    class Meta:
        model = DeviceToken
        fields = [
            "id",
            "token",
            "device_name",
        ]