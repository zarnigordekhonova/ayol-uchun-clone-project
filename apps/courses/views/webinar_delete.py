from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404

from apps.courses.models import Webinar


class WebinarDeleteAPIView(DestroyAPIView):
    queryset = Webinar.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        webinar = get_object_or_404(Webinar, id=self.kwargs["pk"])
        if webinar.author != self.request.user:
            raise PermissionDenied("Siz faqatgina o'zingizga tegishli webinarni o'chirishingiz mumkin!")
        return webinar