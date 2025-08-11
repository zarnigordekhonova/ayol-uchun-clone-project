from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Category
from apps.courses.serializers import GetCategorySerializer


class GetCategoriesAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = GetCategorySerializer
    permission_classes = [IsAuthenticated]