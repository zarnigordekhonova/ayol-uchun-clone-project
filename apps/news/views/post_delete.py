from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import RetrieveDestroyAPIView

from apps.news.models import Post


class PostDeleteAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Bu id dagi post topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({"detail": "Post muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    