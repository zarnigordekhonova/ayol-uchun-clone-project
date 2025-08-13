from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Module
from apps.courses.serializers import GetModulesListSerializer


class GetModulesListAPIView(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = GetModulesListSerializer
    permission_classes = [IsAdminUser]