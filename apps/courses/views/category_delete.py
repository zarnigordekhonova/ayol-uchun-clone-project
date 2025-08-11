from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied

from django.shortcuts import get_object_or_404

from apps.courses.models import Category


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        category = get_object_or_404(Category, id=self.kwargs["pk"])
        if category.author != self.request.user:
            raise PermissionDenied("Siz faqatgina o'zingizga tegishli kategoriyani o'chirishingiz mumkin!")
        return category