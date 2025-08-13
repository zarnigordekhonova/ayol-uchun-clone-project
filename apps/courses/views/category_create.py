from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.courses.serializers import CreateCategorySerializer


class CreateCategoryAPIView(CreateAPIView):
    serializer_class =  CreateCategorySerializer
    permission_classes = [IsAdminUser]

    
    