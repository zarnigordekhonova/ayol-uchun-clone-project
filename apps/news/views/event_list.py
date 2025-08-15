from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import Event
from apps.news.serializers import EventListSerializer


class EventsListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    permission_classes = [IsAuthenticated]