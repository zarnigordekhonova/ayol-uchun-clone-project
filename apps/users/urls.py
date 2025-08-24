from django.urls import path

from apps.users.views import (UserRegisterAPIView, 
                              UserLoginAPIView, 
                              GetProfileAPIView, 
                              UserLogoutAPIView,
                              ActivationAPIView)

app_name = "users"

urlpatterns = [
    path("user-register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("user-login/", UserLoginAPIView.as_view(), name="user-login"),
    path("get-profile/", GetProfileAPIView.as_view(), name="get-profile"),
    path("user-logout/", UserLogoutAPIView.as_view(), name="user-logout"),
    path('activate/<uidb64>/<token>/', ActivationAPIView.as_view(), name='activate'),
]