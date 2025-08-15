from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView

from apps.news.models import Post
from apps.news.serializers import PostUpdateSerializer


class PostUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class =  PostUpdateSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Bu id dagi post topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)