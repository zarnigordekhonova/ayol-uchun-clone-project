from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from django.shortcuts import get_object_or_404

from apps.courses.models import Category
from apps.courses.serializers import UpdateCategorySerializer


class UpdateCategoryAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class =  UpdateCategorySerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        category = get_object_or_404(Category, id=self.kwargs["pk"])
        if category.author !=  self.request.user:
            self.permission_denied(
                self.request,
                message="Siz faqatgina o'zingizga tegishli kategoriyani tahrirlashingiz mumkin!"
            )

        return category
    