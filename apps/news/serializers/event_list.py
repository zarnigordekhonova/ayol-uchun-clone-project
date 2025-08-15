from rest_framework import serializers

from apps.news.models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "card",
            "datetime",
            "location_name",
            "longitude",
            "latitude",
        )