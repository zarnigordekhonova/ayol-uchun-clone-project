from rest_framework import serializers

from apps.courses.models import Webinar


class GetSingleWebinarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Webinar
        fields = (
            "title",
            "description",
            "price",
            "card",
            "category",
            "author",
            "datetime",
            "rating"
        )