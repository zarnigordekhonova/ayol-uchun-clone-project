from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import DestroyAPIView

from apps.news.models import Post


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        try:
            post = self.get_object()
        except Post.DoesNotExist:
            return Response({"detail": "Bu id dagi post topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({"detail": "Post muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)

    