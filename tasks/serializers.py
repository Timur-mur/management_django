from rest_framework import serializers
from .models import Tasks


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_topic",
            "task_executor",
            "task_description",
            "task_deadline",
            "task_status",
            "task_flag",
            "task_file",
        )

class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "id",
            "task_topic",
            "task_description",
            "task_deadline",
            "task_status",
            "task_executor",
            "task_flag",
            "task_file",
        )


class EmployeeGetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_executor",
            "task_status",
        )


class SendTaskToCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_status",
            "task_file",
        )


class AcceptTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_status",
        )


class ReturnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = (
            "task_status",
            "task_flag",
        )