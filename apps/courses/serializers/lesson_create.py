from rest_framework import serializers

from apps.courses.models import Lesson, Module


class LessonCreateGetModuleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Module
        fields = ["name"]


class LessonCreateSerializer(serializers.ModelSerializer):
    module_name =  serializers.CharField(write_only=True)
    module = LessonCreateGetModuleDataSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = (
            "module", # ma'lumotni chiqarishda module nomi bilan chiqadi
            "module_name", # modul nomini kiritishda module_name bilan kiritiladi
            "title",
            "description",
            "file",
            "duration",
        )

    def create(self, validated_data):
        module_name = validated_data.pop("module_name")
        try: 
            module = Module.objects.get(name=module_name)
        except Module.DoesNotExist:
            raise serializers.ValidationError({"module_name": "Bunday nomdagi modul mavjud emas."})
        except Module.MultipleObjectsReturned:
            raise serializers.ValidationError({"module_name": "Bunday nomda bir nechta modul mavjud, aniq nom kiriting."})
        
        lesson = Lesson.objects.create(module=module, **validated_data)
        return lesson