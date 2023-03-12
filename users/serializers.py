from rest_framework import serializers
from .models import CustomUser


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "last_name",
            "role",
            "avatar",
        ]
