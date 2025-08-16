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
    SurveyCreateAPIView,
    SurveysListAPIView,
    SurveyUpdateAPIView,
    SurveyDeleteAPIView,
    # Question
    QuestionCreateAPIView,
    QuestionsListAPIView,
    QuestionDeleteAPIView,
    QuestionUpdateAPIView,
    # QuestionOption
    QuestionOptionCreateAPIView,
    QuestionOptionListAPIView,
    QuestionOptionUpdateAPIView,
    QuestionOptionDeleteAPIView,
    # UserAnswer
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
    path("survey-create/", SurveyCreateAPIView.as_view(), name="survey-create"),
    path("survey-list/", SurveysListAPIView.as_view(), name="survey-list"),
    path("survey/<int:pk>/update/", SurveyUpdateAPIView.as_view(), name="survey-update"),
    path("survey/<int:pk>/delete/", SurveyDeleteAPIView.as_view(), name="survey-delete"),
    # Question
    path("question-create/", QuestionCreateAPIView.as_view(), name="question-create"),
    path("question-list/", QuestionsListAPIView.as_view(), name="question-list"),
    path("question/<int:pk>/update/", QuestionUpdateAPIView.as_view(), name="question-update"),
    path("question/<int:pk>/delete/", QuestionDeleteAPIView.as_view(), name="question-delete"),
    # QuestionOption
    path("question-option-create/", QuestionOptionCreateAPIView.as_view(), name="question-option-create"),
    path("question-option-list/", QuestionOptionListAPIView.as_view(), name="question-option-list"),
    path("question-option/<int:pk>/update/", QuestionOptionUpdateAPIView.as_view(), name="question-option-update"),
    path("question-option/<int:pk>/delete/", QuestionOptionDeleteAPIView.as_view(), name="question-option-delete"),
    # UserAnswer
    
]