from rest_framework import serializers
from .models import CustomUser


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "role",
            "avatar",
        ]


class UserFillInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "avatar",
        ]
class Edit_Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "role",
        ]


class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
        ]