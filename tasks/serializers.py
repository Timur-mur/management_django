from rest_framework import serializers
from .models import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "task_topic",
            "task_executors",
            "task_number_of_performing",
            "task_description",
            "task_deadline",
            "task_status",
            "task_flag",
            "task_file",
        )

class GetTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "task_topic",
            "task_count_of_performing",
            "task_description",
            "task_deadline",
            "task_status",
            "task_executors",
            "task_flag",
            "task_file",
        )