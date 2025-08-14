from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from django.shortcuts import get_object_or_404

from apps.courses.models import Course
from apps.courses.serializers import CourseUpdateSerializer


class UpdateCourseAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class =  CourseUpdateSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        if course.author !=  self.request.user:
            self.permission_denied(
                self.request,
                message="Siz faqatgina o'zingizga tegishli kursni tahrirlashingiz mumkin!"
            )

        return course
    