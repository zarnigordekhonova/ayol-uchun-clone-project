from rest_framework import serializers

from apps.courses.models import Comment


class CommentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(read_only=True)
    rating = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)

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


