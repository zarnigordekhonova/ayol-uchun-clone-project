from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.courses.models import Course, Webinar
from apps.courses.serializers import CourseCommentsListSerializer, WebinarCommentsListSerializer


class GetCourseCommentsListAPIView(APIView):
    permission_classes = [IsAdminUser | IsAuthenticated]

    def post(self, request):
        title = request.data.get("title") # Course nomi body orqali beriladi
        if not title:
            return Response({"detail": "Course title is required in body."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.prefetch_related('comments').get(title=title)
        except Course.DoesNotExist:
            return Response({"detail": "Bu nomdagi kurs topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseCommentsListSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)        


class GetWebinarCommentsListAPIView(APIView):
    permission_classes = [IsAdminUser | IsAuthenticated]

    def post(self, request):
        title = request.data.get("title")
        if not title:
            return Response({"detail": "Webinar title is required in body."})
        
        try:
            webinar = Webinar.objects.prefetch_related("comments").get(title=title)
        except Webinar.DoesNotExist:
            return Response({"detail": "Bu nomdagi webinar topilmadi."})
        
        serializer = WebinarCommentsListSerializer(webinar)
        return Response(serializer.data, status=status.HTTP_200_OK)
