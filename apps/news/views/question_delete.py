from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import DestroyAPIView

from apps.news.models import Question


class QuestionDeleteAPIView(DestroyAPIView):
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        try:
            question = self.get_object()
        except Question.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma savoli topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response({"detail": "So'rovnoma savoli muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    