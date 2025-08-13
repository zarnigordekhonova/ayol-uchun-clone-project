from rest_framework import serializers

from apps.courses.models import Comment, Course, Webinar

class CommentGetCourseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Course
        fields = ["title"]


class GetWebinarDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ["title"]


class CourseCommentCreateSerializer(serializers.ModelSerializer):
    course_name =  serializers.CharField(write_only=True)
    course = CommentGetCourseDataSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "course", # ma'lumotni chiqarishda kurs nomi bilan chiqadi
            "course_name", # kurs nomini kiritishda course_name bilan kiritiladi
            "text",
            "rating",
        )

    def create(self, validated_data):
        course_name = validated_data.pop("course_name")
        try: 
            course = Course.objects.get(title=course_name)
        except Course.DoesNotExist:
            raise serializers.ValidationError({"course_name": "Bunday nomdagi kurs mavjud emas."})
        except Course.MultipleObjectsReturned:
            raise serializers.ValidationError({"course_name": "Bunday nomda bir nechta kurs mavjud, aniq nom kiriting."})
        
        comment = Comment.objects.create(course=course, **validated_data)
        return comment
    
    def to_representation(self, instance):
        return {
            "user": {
                "id": instance.user.id,
                "username": instance.user.username
            },
            "course": instance.course.title, 
            "text": instance.text,
            "rating": instance.rating,
        }

    

class WebinarCommentCreateSerializer(serializers.ModelSerializer):
    webinar_name =  serializers.CharField(write_only=True)
    webinar = GetWebinarDataSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "webinar", # ma'lumotni chiqarishda webinar nomi bilan chiqadi
            "webinar_name", # webinar nomini kiritishda webinar_name bilan kiritiladi
            "text",
            "rating",
        )

    def create(self, validated_data):
        webinar_name = validated_data.pop("webinar_name")
        try: 
            webinar = Webinar.objects.get(title=webinar_name)
        except Webinar.DoesNotExist:
            raise serializers.ValidationError({"webinar_name": "Bunday nomdagi webinar mavjud emas."})
        except Webinar.MultipleObjectsReturned:
            raise serializers.ValidationError({"webinar_name": "Bunday nomda bir nechta webinar mavjud, aniq nom kiriting."})
        
        comment = Comment.objects.create(webinar=webinar, **validated_data)
        return comment
    
    def to_representation(self, instance):
        return {
            "user": {
                "id": instance.user.id,
                "username": instance.user.username
            },
            "webinar": instance.webinar.title, 
            "text": instance.text,
            "rating": instance.rating,
        }
