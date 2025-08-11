from rest_framework import serializers

from apps.courses.models import Webinar


class WebinarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Webinar
        fields = (
            "title",
            "description",
            "price",
            "card", 
            "category",
            "author",
            "rating",
            "datetime",
            "status"
        )