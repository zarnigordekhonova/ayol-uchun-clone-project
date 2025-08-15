from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Course, Webinar, Comment


class DeleteCourseCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        title = request.data.get("title")
        if not title:
            return Response({"detail": "Course title is required in body"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(title=title)
        except Course.DoesNotExist:
            return Response({"detail": "Bu nomdagi kurs mavjud emas."}, status=status.HTTP_404_NOT_FOUND)

        try:
            comment = course.comments.get(user=request.user)
        except Comment.DoesNotExist:
            return Response({"detail": "Siz bu kurs uchun sharh qoldirmagansiz."}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response({"detail": "Sharh muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)
    

class DeleteWebinarCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        title = request.data.get("title")

        if not title:
            return Response({"detail": "Webinar title is required in body."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            webinar = Webinar.objects.get(title=title)
        except Webinar.DoesNotExist:
            return Response({"detail": "Bu nomdagi vebinar mavjud emas."}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            comment = webinar.comments.get(user=request.user)
        except Comment.DoesNotExist:
            return Response({"detail": "Siz bu vebinar uchun sharh qoldirmagansiz."}, status=status.HTTP_404_NOT_FOUND)
        
        comment.delete()
        return Response({"detail": "Sharh muvaffaqiyatli o'chirildi."}, status=status.HTTP_200_OK)
