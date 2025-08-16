from rest_framework import serializers

from apps.news.models import Question, QuestionOption


class QuestionOptionGetQestionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["title"]


class QuestionOptionListSerializer(serializers.ModelSerializer):
    question = QuestionOptionGetQestionDataSerializer(read_only=True)

    class Meta:
        model = QuestionOption
        fields = (
            "question",
            "title",
        )