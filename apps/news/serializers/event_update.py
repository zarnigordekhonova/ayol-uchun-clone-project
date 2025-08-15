from rest_framework import serializers

from apps.news.models import Event


class EventUpdateSerializer(serializers.ModelSerializer):
    longitude = serializers.FloatField(read_only=True)
    latitude = serializers.FloatField(read_only=True)

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

    def to_representation(self, instance):
        return {
            "title": instance.title,
            "description" : instance.description,
            "card": instance.card,
            "datetime" : instance.datetime,
            "location_name" : instance.location_name,
            "longitude" : instance.longitude,
            "latitude" : instance.latitude,
        }