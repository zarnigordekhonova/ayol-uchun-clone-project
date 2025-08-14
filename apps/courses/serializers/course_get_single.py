from rest_framework import serializers

from apps.courses.models import Course, Module, Lesson


class CourseModulesLessonsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = (
            "title",
            "description",
            "file",
            "duration",
        )


class CourseModulesSerializer(serializers.ModelSerializer):
    lessons = CourseModulesLessonsSerializer(read_only=True, many=True)
    
    class Meta:
        model = Module
        fields = (
            "name",
            "lessons",
        )


class GetSingleCourseSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)
    module = CourseModulesSerializer(many=True, source='modules', read_only=True)


    class Meta:
        model = Course
        fields = (
            "card", 
            "title", 
            "description", 
            "author_first_name",
            "author_last_name", 
            "category", 
            "module",
            "price",
            "rating",
        )