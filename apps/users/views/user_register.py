from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
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
        activation_link = f"{scheme}://{current_site}/api/users/activate/{uid}/{token}/"

        html_content = render_to_string('email/activation_email.html', {
            'user': user,
            'activation_link': activation_link
        })

        send_mail(
            subject="Akkountingizni faollashtiring",
            message="Your email client does not support HTML. Please click the link.",
            from_email="zarnigor1008@gmail.com",
            recipient_list=[user.email],
            html_message=html_content,
        )
        print("User email", user.email)
        print("After sending email", activation_link)
        return Response({"detail": "Activation email sent. Please check your inbox."}, status=201)



        