from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Webinar
from apps.courses.serializers import GetWebinarsSerializer


class GetWebinarsView(ListAPIView):
    queryset = Webinar.objects.all()
    serializer_class = GetWebinarsSerializer
    permission_classes = [IsAuthenticated]
    