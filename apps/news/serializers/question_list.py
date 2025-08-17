from rest_framework import serializers

from apps.news.models import Question, Survey


class QuestionListGetSurveyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ["title"]


class QuestionsListSerializer(serializers.ModelSerializer):
    survey = QuestionListGetSurveyDataSerializer(read_only=True)

    class Meta:
        model = Question
        fields = (
            "survey",
            "title",
            "type",
            "file",
        )