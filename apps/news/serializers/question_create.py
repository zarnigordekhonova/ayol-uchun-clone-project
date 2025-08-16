from rest_framework import serializers

from apps.news.models import Question, Survey
from apps.news.choices import QuestionTypeChoices


class QuestionCreateSerializer(serializers.ModelSerializer):
    survey = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=QuestionTypeChoices.choices, required=True)

    class Meta:
        model = Question
        fields = (
            "survey",
            "title",
            "type",
            "file"
        )

    def create(self, validated_data):
        survey_name = validated_data.pop("survey")
        try: 
            survey = Survey.objects.get(title=survey_name)
        except Survey.DoesNotExist:
            raise serializers.ValidationError({"Survey": "Bunday nomdagi so'rovnoma mavjud emas."})
        except Survey.MultipleObjectsReturned:
            raise serializers.ValidationError({"Survey": "Bunday nomda bir nechta so'rovnoma mavjud, aniq nom kiriting."})
        
        question = Question.objects.create(survey=survey, **validated_data)
        return question