from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404

from apps.courses.models import Course


class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        course = get_object_or_404(Course, id=self.kwargs["pk"])
        if course.author != self.request.user:
            raise PermissionDenied("Siz faqatgina o'zingizga tegishli kursni o'chirishingiz mumkin!")
        return course