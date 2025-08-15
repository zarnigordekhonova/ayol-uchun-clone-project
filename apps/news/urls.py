from django.urls import path

from apps.news.views import (
    # Post
    PostCreateAPIView,
    PostsListAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    # Event
    EventCreateAPIView,
    EventsListAPIView,
    EventUpdateAPIView,
    EventDeleteAPIView,
    # Survey
)

app_name = "news"

urlpatterns = [
    # Post
    path("post-create/", PostCreateAPIView.as_view(), name="post-create"),
    path("post-list/", PostsListAPIView.as_view(), name="post-list"),
    path("post/<int:pk>/update/", PostUpdateAPIView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteAPIView.as_view(), name="post-delete"),
    # Event
    path("event-create/", EventCreateAPIView.as_view(), name="event-create"),
    path("event-list/", EventsListAPIView.as_view(), name="event-list"),
    path("event/<int:pk>/update/", EventUpdateAPIView.as_view(), name="event-update"),
    path("event/<int:pk>/delete/", EventDeleteAPIView.as_view(), name="event-delete"),
    # Survey
]