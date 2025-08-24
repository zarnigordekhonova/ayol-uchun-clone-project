from rest_framework import serializers

from apps.courses.models import Module, Course


class GetCourseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["title"]


class ModuleUpdateSerializer(serializers.ModelSerializer):
    course = GetCourseDataSerializer(read_only=True)

    class Meta:
        model = Module
        fields = (
            "course",
            "name",
            "icon"
        )

    def update(self, instance, validated_data):
        course_name = validated_data.pop("course", None)
        try: 
            course = Course.objects.get(title=course_name)
        except Course.DoesNotExist:
            raise serializers.ValidationError({"Course": "Bunday nomdagi kurs mavjud emas."})
        except Course.MultipleObjectsReturned:
            raise serializers.ValidationError({"Course": "Bunday nomda bir nechta kurs mavjud, aniq nom kiriting."})
        
        instance.course = course
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance