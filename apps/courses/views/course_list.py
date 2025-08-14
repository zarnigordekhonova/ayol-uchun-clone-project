from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Course
from apps.courses.serializers import GetCoursesSerializer


class GetCoursesView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = GetCoursesSerializer
    permission_classes = [IsAuthenticated]