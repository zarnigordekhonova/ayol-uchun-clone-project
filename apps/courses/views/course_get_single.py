from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Course
from apps.courses.serializers import GetSingleCourseSerializer


class GetSingleCourseAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = GetSingleCourseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
