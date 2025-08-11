from rest_framework import serializers

from apps.courses.models import Course


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Course
        fields = (
            "title",
            "description",
            "price",
            "card", 
            "category",
            "rating",
        )