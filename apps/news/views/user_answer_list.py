from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.news.models import UserAnswer
from apps.news.serializers import UserAnswersListSerializer


class UserAnswerListAPIView(ListAPIView):
    '''
    Buyerda agar request user admin bo'lsa unga
    hamma userlarning tanlagan javoblari ko'rinadi,
    agar u oddiy user bo'lsa, unga faqat o'zi 
    tanlagan javoblar ko'rinadi.
    '''
    serializer_class = UserAnswersListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return UserAnswer.objects.all()
        return UserAnswer.objects.filter(user=user)
    

