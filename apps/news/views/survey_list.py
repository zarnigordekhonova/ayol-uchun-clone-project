from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import Survey
from apps.news.serializers import GetSurveysListSerializer


class SurveysListAPIView(ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = GetSurveysListSerializer
    permission_classes = [IsAuthenticated]