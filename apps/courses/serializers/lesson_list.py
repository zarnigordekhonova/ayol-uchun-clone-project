from rest_framework import serializers

from apps.courses.models import Lesson, Module


class GetModuleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["name"]


class GetLessonListSerializer(serializers.ModelSerializer):
    module = GetModuleDataSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "module",
            "title",
            "description",
            "file",
            "duration",
        )
