from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Module


class ModuleDeleteAPIView(DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [IsAdminUser]

    