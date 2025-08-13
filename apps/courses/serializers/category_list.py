from rest_framework import serializers

from apps.courses.models import Category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "icon"
        )