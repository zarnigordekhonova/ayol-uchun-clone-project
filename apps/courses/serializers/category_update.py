from rest_framework import serializers

from apps.courses.models import Category


class UpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "icon"
        )