from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView

from apps.news.models import Survey


class SurveyDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            survey = Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        survey.delete()
        return Response({"detail": "So'rovnoma muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    