from rest_framework import serializers

from apps.courses.models import Lesson, Module


class LessonUpdateGetModuleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["name"]


class LessonUpdateSerializer(serializers.ModelSerializer):
    module = LessonUpdateGetModuleDataSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "module",
            "title",
            "description",
            "file",
            "duration",
        )

    def create(self, validated_data):
        module_name = validated_data.pop("module")
        try: 
            module = Lesson.objects.get(title=module_name)
        except Lesson.DoesNotExist:
            raise serializers.ValidationError({"Lesson": "Bunday nomdagi modul mavjud emas."})
        except Lesson.MultipleObjectsReturned:
            raise serializers.ValidationError({"Lesson": "Bunday nomda bir nechta modul mavjud, aniq nom kiriting."})
        
        lesson = Lesson.objects.create(module=module, **validated_data)
        return lesson