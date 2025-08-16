from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView

from apps.news.models import Question


class QuestionDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma savoli topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response({"detail": "So'rovnoma savoli muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    