from rest_framework import serializers

from apps.courses.models import Webinar
from apps.courses.choices import WebinarStatusChoices


class FinishWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ['status']

    def update(self, instance, validated_data):
        instance.status = WebinarStatusChoices.FINISHED
        instance.save(update_fields=['status'])

        return instance