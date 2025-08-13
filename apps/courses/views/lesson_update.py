from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.courses.models import Lesson
from apps.courses.serializers import LessonUpdateSerializer


class LessonUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class =  LessonUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response({"detail": "Bu id dagi lesson topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)