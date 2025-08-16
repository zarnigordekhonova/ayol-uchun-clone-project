from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.news.models import Question
from apps.news.serializers import QuestionUpdateSerializer


class QuestionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class =  QuestionUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma savoli topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)