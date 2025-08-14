from rest_framework import serializers

from apps.courses.models import Course


class GetCoursesSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)
                                    

    class Meta:
        model = Course
        fields = (
            "card", 
            "title",  
            "author_first_name",
            "author_last_name", 
            "category", 
            "price",
        )