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

    def update(self, instance, validated_data):
        module_name = validated_data.pop("module", None)
        try: 
            module = Module.objects.get(name=module_name)
        except Module.DoesNotExist:
            raise serializers.ValidationError({"Lesson": "Bunday nomdagi modul mavjud emas."})
        except Module.MultipleObjectsReturned:
            raise serializers.ValidationError({"Lesson": "Bunday nomda bir nechta modul mavjud, aniq nom kiriting."})
        
        instance.module = module
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
