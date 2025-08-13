from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.serializers import CourseCommentCreateSerializer, WebinarCommentCreateSerializer


class CourseCreateCommentAPIView(CreateAPIView):
    serializer_class =  CourseCommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class WebinarCreateCommentAPIView(CreateAPIView):
    serializer_class =  WebinarCommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)