from django.urls import path

from apps.courses.views import (GetCoursesView,
                                GetWebinarsView,
                                GetSingleCourseAPIView,
                                )

app_name = "courses"

urlpatterns = [
    path("get-courses/", GetCoursesView.as_view(), name="get-courses"),
    path("get-webinars/", GetWebinarsView.as_view(), name="get-webinars"),
    path("get/<int:pk>/course", GetSingleCourseAPIView.as_view(), name="get-single-course")
]