from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import Question
from apps.news.serializers import QuestionsListSerializer


class QuestionsListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionsListSerializer
    permission_classes = [IsAuthenticated]