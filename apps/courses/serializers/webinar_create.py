from rest_framework import serializers

from apps.courses.models import Webinar


class WebinarCreateSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model =  Webinar
        fields = (
            "title",
            "description",
            "price",
            "card", 
            "category",
            "rating",
            "datetime",
            "status"
        )