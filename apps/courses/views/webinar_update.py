from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404

from apps.courses.models import Webinar
from apps.courses.serializers import WebinarUpdateSerializer


class UpdateWebinarAPIView(UpdateAPIView):
    queryset = Webinar.objects.all()
    serializer_class =  WebinarUpdateSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get_object(self):
        webinar = get_object_or_404(Webinar, id=self.kwargs["pk"])
        if webinar.author !=  self.request.user:
            self.permission_denied(
                self.request,
                message="Siz faqatgina o'zingizga tegishli webinarni tahrirlashingiz mumkin!"
            )

        return webinar
    