from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Lesson


class LessonDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]

    