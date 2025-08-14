from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from apps.courses.models import Webinar
from apps.courses.serializers import FinishWebinarSerializer


class FinishWebinarAPIView(UpdateAPIView):
    queryset = Webinar.objects.all()
    serializer_class =  FinishWebinarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        webinar = get_object_or_404(Webinar, id=self.kwargs["pk"])
        if webinar.author !=  self.request.user:
            self.permission_denied(
                self.request,
                message="Siz faqatgina o'zingizga tegishli webinarni tugatishingiz mumkin!"
            )

        return webinar
    
    def update(self, request, *args, **kwargs):
        webinar = self.get_object()

        if webinar.status == "finished":
            return Response({"detail": "Bu webinar allaqachon tugatilgan"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(webinar, data={}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"detail": "Webinar muvaffaqiyatli tugatildi."}, status=status.HTTP_200_OK)