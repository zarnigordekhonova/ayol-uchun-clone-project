from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import DestroyAPIView

from apps.news.models import Event


class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [IsAdminUser]
    
    def delete(self, request, *args, **kwargs):
        try:
            event = self.get_object()
        except Event.DoesNotExist:
            return Response({"detail": "Bu id dagi tadbir topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        event.delete()
        return Response({"detail": "Tadbir muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)