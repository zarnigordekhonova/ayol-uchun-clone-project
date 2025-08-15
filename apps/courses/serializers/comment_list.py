from rest_framework import serializers

from apps.courses.models import Course, Webinar, Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "text",
            "rating"
        )

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "user": instance.user.username,
            "text": instance.text,
            "rating": instance.rating,
        }


class CourseCommentsListSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True) 

    class Meta:
        model = Course
        fields = (
            "title", 
            "comments",
        )
    

class WebinarCommentsListSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True) 

    class Meta:
        model = Webinar
        fields = (
            "title", 
            "comments"
        )

   