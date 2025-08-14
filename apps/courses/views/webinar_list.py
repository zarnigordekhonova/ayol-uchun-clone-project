from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import Webinar
from apps.courses.choices import WebinarStatusChoices
from apps.courses.serializers import GetWebinarsSerializer


class GetWebinarsAPIView(ListAPIView):
    serializer_class = GetWebinarsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = self.request.query_params.get("status")
        queryset = Webinar.objects.all()

        if status_param and status_param != "all":  # http://127.0.0.1:8000/api/v1/courses/get-webinars/?status=upcoming
            valid_statuses = dict(WebinarStatusChoices.choices).keys()   # statusga qarab, webinarlarni filter qilib chiqaradi
            if status_param.lower() in valid_statuses:                   # ?status=all bo'lsa, hamma webinarlar chiqadi, upcoming bo'lsa ham, live bo'lsa ham     
                return Webinar.objects.filter(status=status_param.lower())
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"detail": "No webinars found for the chosen status"},
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    