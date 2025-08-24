from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator

from apps.users.serializers import UserRegisterSerializer

CustomUser = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        scheme = "https" if request.is_secure() else "http"
        current_site = request.get_host()
        activation_link = f"{scheme}://{current_site}/users/activate/{uid}/{token}/"

        html_content = render_to_string('email/activation_email.html', {
            'user': user,
            'activation_link': activation_link
        })
        text_content = f"Please click the link to activate your account: {activation_link}"

        email = EmailMultiAlternatives(
            subject="Akkountingizni faollashtiring",
            body=text_content,
            from_email="zarnigor1008@gmail.com",
            to=[user.email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        
        return Response({"detail": "Activation email sent. Please check your inbox."}, status=201)



        