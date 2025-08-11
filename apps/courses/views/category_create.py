from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.courses.serializers import CreateCategorySerializer


class CreateCategoryAPIView(CreateAPIView):
    serializer_class =  CreateCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    