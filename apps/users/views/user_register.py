from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    model 