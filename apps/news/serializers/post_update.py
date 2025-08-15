from rest_framework import serializers

from apps.news.models import Post


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "description",
            "card"
        )