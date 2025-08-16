from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView

from apps.news.models import QuestionOption


class QuestionOptionDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            question_option = QuestionOption.objects.get(pk=pk)
        except QuestionOption.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma savoli varianti topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        question_option.delete()
        return Response({"detail": "So'rovnoma savoli varianti muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    