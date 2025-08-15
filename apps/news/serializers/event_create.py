from rest_framework import serializers

from apps.news.models import Event


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "title",
            "description",
            "card",
            "location_name",
        )