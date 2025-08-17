from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.news.models import Event
from apps.news.serializers import EventUpdateSerializer


class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class =  EventUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            post = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"detail": "Bu id dagi tadbir topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)