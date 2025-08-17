from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.news.serializers import EventCreateSerializer


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Event muvaffaqiyatli qo'shildi.", "data" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"detail": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)