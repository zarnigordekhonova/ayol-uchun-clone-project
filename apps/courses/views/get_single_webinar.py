from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Webinar
from apps.courses.serializers import GetSingleWebinarSerializer


class GetSingleWebinarAPIView(RetrieveAPIView):
    serializer_class = GetSingleWebinarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            course = Webinar.objects.get(pk=pk)
        except Webinar.DoesNotExist:
            return Response({"detail": "Webinar not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
