from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.news.models import Post
from apps.news.serializers import PostListSerializer


class PostsListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]