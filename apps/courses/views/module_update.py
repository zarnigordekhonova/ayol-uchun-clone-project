from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404

from apps.courses.models import Module
from apps.courses.serializers import ModuleUpdateSerializer


class ModuleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Module.objects.all()
    serializer_class =  ModuleUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            module = Module.objects.get(pk=pk)
        except Module.DoesNotExist:
            return Response({"detail": "Bu id dagi modul topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(module)
        return Response(serializer.data, status=status.HTTP_200_OK)