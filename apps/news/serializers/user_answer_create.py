from rest_framework import serializers

from apps.news.models import UserAnswer, Question, QuestionOption


class UserAnswerCreateSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        write_only=True
    )

    chosen_option_title = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = UserAnswer
        fields = ("question", "chosen_option_title", "text_answer")

    def validate(self, attrs):
        question = attrs.get("question")
        chosen_option_title = attrs.get("chosen_option_title", "").strip()
        text_answer = attrs.get("text_answer", "").strip()

        if question.type == "open_answer":
            if not text_answer:
                raise serializers.ValidationError({
                    "text_answer": "Bu savol uchun javobni o'zingiz kiritishingiz kerak."
                })
            if chosen_option_title:
                raise serializers.ValidationError({
                    "chosen_option_title": "Ochiq savollar uchun variant belgilash mumkin emas!."
                })
        else:
            if not chosen_option_title:
                raise serializers.ValidationError({
                    "chosen_option_title": "Bu savol uchun javob sifatida variant tanlashingiz kerak."
                })
            if text_answer:
                raise serializers.ValidationError({
                    "text_answer": "Yopiq savollar uchun matnli javob kiritish mumkin emas!"
                })
            if not QuestionOption.objects.filter(question=question, title=chosen_option_title).exists():
                raise serializers.ValidationError({
                    "chosen_option_title": "Bu savol uchun bunday variant mavjud emas."
                })

        return attrs

    def create(self, validated_data):
        chosen_option_title = validated_data.pop("chosen_option_title", "").strip()
        question = validated_data["question"]

        chosen_option_obj = None
        if question.type != "open_answer":
            chosen_option_obj = QuestionOption.objects.get(
                question=question,
                title=chosen_option_title
            )

        user_answer = UserAnswer.objects.create(
            user=validated_data["user"],
            question=question,
            chosen_option=chosen_option_obj,
            text_answer=validated_data.get("text_answer", "")
        )
        return user_answer

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "user": {
                "username" : instance.user.username
            },
            "question": {
                "id": instance.question.id,
                "title": instance.question.title,
                "type": instance.question.type,
            },
            "chosen_option": (
                {
                    "id": instance.chosen_option.id,
                    "title": instance.chosen_option.title,
                }
                if instance.chosen_option
                else None
            ),
            "text_answer": instance.text_answer,
        }
