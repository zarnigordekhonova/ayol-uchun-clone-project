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

    def create(self, validated_data):
        course_name = validated_data.pop("course")
        try: 
            course = Module.objects.get(title=course_name)
        except Module.DoesNotExist:
            raise serializers.ValidationError({"Course": "Bunday nomdagi kurs mavjud emas."})
        except Module.MultipleObjectsReturned:
            raise serializers.ValidationError({"Course": "Bunday nomda bir nechta kurs mavjud, aniq nom kiriting."})
        
        module = Module.objects.create(course=course, **validated_data)
        return module