from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model

from apps.users.serializers import UserRegisterSerializer

CustomUser = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny, ]