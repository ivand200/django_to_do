from rest_framework import serializers

from .models import Task, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "done", "done_date"]


class TaskSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "created_date", "jobs", "user"]
        read_only_fields = ("user",)
