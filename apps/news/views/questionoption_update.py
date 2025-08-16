from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.news.models import QuestionOption
from apps.news.serializers import QuestionOptionUpdateSerializer


class QuestionOptionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class =  QuestionOptionUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            question_option = QuestionOption.objects.get(pk=pk)
        except QuestionOption.DoesNotExist:
            return Response({"detail": "Bu id dagi so'rovnoma savoli varianti topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(question_option)
        return Response(serializer.data, status=status.HTTP_200_OK)