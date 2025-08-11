from rest_framework import serializers

from apps.courses.models import Category


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "title",
            "icon"
        )