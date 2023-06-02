from rest_framework import serializers
from .models import Chat


class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'user_id',
            'type',
            'text',
            'send_time',
        )


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'user_id',
            'type',
            'text',
            'send_time',
        )