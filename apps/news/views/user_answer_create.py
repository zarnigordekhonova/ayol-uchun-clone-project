from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import UserAnswer
from apps.news.serializers import UserAnswerCreateSerializer


class UserAnswerCreateAPIView(CreateAPIView):
    serializer_class = UserAnswerCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
