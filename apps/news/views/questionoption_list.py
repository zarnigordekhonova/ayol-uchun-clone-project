from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import QuestionOption
from apps.news.serializers import QuestionOptionListSerializer


class QuestionOptionListAPIView(ListAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionListSerializer
    permission_classes = [IsAuthenticated]