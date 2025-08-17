from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.news.models import QuestionOption
from apps.news.serializers import QuestionOptionCreateSerializer


class QuestionOptionCreateAPIView(CreateAPIView):
    serializer_class = QuestionOptionCreateSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_option = serializer.save()
        return Response(
            {
                "message": "So'rovnoma savoli varianti muvaffaqiyatli qo'shildi.",
                "data": QuestionOptionCreateSerializer(question_option).data
            },
            status=status.HTTP_201_CREATED
        ) 

