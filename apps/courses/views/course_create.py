from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.serializers import CourseCreateSerializer


class CreateCourseAPIView(CreateAPIView):
    serializer_class =  CourseCreateSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    