from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import GetProfileSerializer


class GetProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = GetProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
    