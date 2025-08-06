from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

CustomUser = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    
    phone_number = serializers(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    role = serializers.CharField(read_only=True)
    class Meta:
        model =  CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "email",
            "password",
            "avatar",
            "bio",
            "interests",
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"