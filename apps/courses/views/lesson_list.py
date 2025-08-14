from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Lesson
from apps.courses.serializers import GetLessonListSerializer


class GetLessonsListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = GetLessonListSerializer
    permission_classes = [IsAdminUser]