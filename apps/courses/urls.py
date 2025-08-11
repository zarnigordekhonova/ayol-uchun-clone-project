from django.urls import path

from apps.courses.views import (GetCoursesView,
                                GetWebinarsView,
                                )

app_name = "courses"

urlpatterns = [
    path("get-courses/", GetCoursesView.as_view(), name="get-courses"),
    path("get-webinars/", GetWebinarsView.as_view(), name="get-webinars"),
]