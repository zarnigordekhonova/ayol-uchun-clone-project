from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Course, Webinar, Comment
from apps.courses.serializers import CommentUpdateSerializer


class UpdateCourseCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        title = request.data.get("title")
        new_text = request.data.get("text")

        if not title or not new_text:
            return Response({"detail": "Both 'title' and 'text' are required in body"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(title=title)
        except Course.DoesNotExist:
            return Response({"detail": "Bu nomdagi kurs mavjud emas."}, status=status.HTTP_404_NOT_FOUND)

        try:
            comment = course.comments.get(user=request.user)
        except Comment.DoesNotExist:
            return Response({"detail": "Siz bu kurs uchun sharh qoldirmagansiz."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentUpdateSerializer(comment, data={"text": new_text}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateWebinarCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        title = request.data.get("title")
        new_text = request.data.get("text")

        if not title or not new_text:
            return Response({"detail": "Both 'title' and 'text' are required in body"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            webinar = Webinar.objects.get(title=title)
        except Webinar.DoesNotExist:
            return Response({"detail": "Bu nomdagi webinar mavjud emas."}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            comment = webinar.comments.get(user=request.user)
        except Comment.DoesNotExist:
            return Response({"detail": "Siz bu vebinar uchun sharh qoldirmagansiz."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentUpdateSerializer(comment, data={"text": new_text}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
