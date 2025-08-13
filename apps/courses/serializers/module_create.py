from rest_framework import serializers

from apps.courses.models import Module, Course


class ModuleCreateSerializer(serializers.ModelSerializer):
    course = serializers.CharField(write_only=True)

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
            course = Course.objects.get(title=course_name)
        except Course.DoesNotExist:
            raise serializers.ValidationError({"Course": "Bunday nomdagi kurs mavjud emas."})
        except Course.MultipleObjectsReturned:
            raise serializers.ValidationError({"Course": "Bunday nomda bir nechta kurs mavjud, aniq nom kiriting."})
        
        module = Module.objects.create(course=course, **validated_data)
        return module