from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Lesson
from apps.courses.serializers import LessonCreateSerializer


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonCreateSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lesson = serializer.save()
        return Response(
            {
                "message": "Dars muvaffaqiyatli qo'shildi.",
                "data": LessonCreateSerializer(lesson).data
            },
            status=status.HTTP_201_CREATED
        )
