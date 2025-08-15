from rest_framework import serializers

from apps.news.models import Survey
from apps.courses.models import Course


class SurveyListGetCourseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title"]


class GetSurveysListSerializer(serializers.ModelSerializer):
    course = SurveyListGetCourseDataSerializer(read_only=True)

    class Meta:
        model = Survey
        fields = (
            "course",
            "id",
            "title",
            "description",
            "card",
        )
