from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404

from apps.news.models import UserAnswer
from apps.news.serializers import UserAnswerUpdateSerializer


class UserAnswerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_answer = get_object_or_404(UserAnswer, id=self.kwargs["pk"])
        if user_answer.user !=  self.request.user:
            self.permission_denied(
                self.request,
                message="Siz faqatgina o'zingizga tegishli javoblarni tahrirlashingiz mumkin!"
            )

        return user_answer


