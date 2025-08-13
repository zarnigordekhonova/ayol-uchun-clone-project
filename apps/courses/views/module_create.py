from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.courses.models import Module
from apps.courses.serializers import ModuleCreateSerializer


class ModuleCreateAPIView(CreateAPIView):
    serializer_class = ModuleCreateSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        module = serializer.save()
        return Response(
            {
                "message": "Modul muvaffaqiyatli qo'shildi.",
                "data": ModuleCreateSerializer(module).data
            },
            status=status.HTTP_201_CREATED
        )
