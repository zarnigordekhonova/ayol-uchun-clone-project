from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.news.models import Survey
from apps.news.serializers import SurveyUpdateSerializer


class SurveyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Survey.objects.all()
    serializer_class =  SurveyUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            survey = Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(survey)
        return Response(serializer.data, status=status.HTTP_200_OK)