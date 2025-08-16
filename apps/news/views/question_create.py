from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.news.serializers import QuestionCreateSerializer


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()
        return Response(
            {
                "message": "So'rovnoma savoli muvaffaqiyatli qo'shildi.",
                "data": QuestionCreateSerializer(question).data
            },
            status=status.HTTP_201_CREATED
        )
