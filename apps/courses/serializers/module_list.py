from rest_framework import serializers

from apps.courses.models import Module, Course


class ModuleListGetCourseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title"]


class GetModulesListSerializer(serializers.ModelSerializer):
    course = ModuleListGetCourseDataSerializer(read_only=True)

    class Meta:
        model = Module
        fields = (
            "course",
            "name",
            "icon"
        )
