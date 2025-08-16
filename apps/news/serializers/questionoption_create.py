from rest_framework import serializers

from apps.news.models import Question, QuestionOption


class QuestionOptionCreateSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        write_only=True
    )

    class Meta:
        model = QuestionOption
        fields = (
            "question",
            "title",
        )

    def to_representation(self, instance):
        return {
            "question" : {
                "id" : instance.question.id,
                "title": instance.question.title
            },
            "title" : instance.title,
        }
