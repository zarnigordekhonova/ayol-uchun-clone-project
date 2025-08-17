from rest_framework import serializers

from apps.users.models import CustomUser
from apps.news.models import Question, QuestionOption, UserAnswer


class UserAnswerGetQuestionDataSerializer(serializers.ModelSerializer):
    survey = serializers.CharField(source="survey.title", read_only=True)

    class Meta:
        model = Question
        fields = (
            "survey",
            "title",
            "type",
            "file",
        )


class UserAnswersListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    question = UserAnswerGetQuestionDataSerializer(read_only=True)
    chosen_option = serializers.CharField(source="chosen_option.title", read_only=True)

    class Meta:
        model = UserAnswer
        fields = (
            "user",
            "question",
            "chosen_option",
            "text_answer"
        )