from rest_framework import serializers

from apps.courses.models import Course


class CourseCreateSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model =  Course
        fields = (
            "title",
            "description",
            "price",
            "card", 
            "category",
        )

    def to_representation(self, instance):
        return {
            "title": instance.title,
            "description" : instance.description,
            "price" : instance.price,
            "card" : instance.card,
            "category" : instance.category,
            "rating": instance.rating
        }