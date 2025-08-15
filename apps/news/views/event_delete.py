from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView

from apps.news.models import Event


class EventDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            post = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response({"detail": "Bu id dagi tadbir topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({"detail": "Tadbir muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    