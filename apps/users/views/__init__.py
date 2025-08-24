from .user_register import UserRegisterAPIView
from .user_login import UserLoginAPIView
from .get_profile import GetProfileAPIView
from .logout import UserLogoutAPIView
from .activation_link import ActivationAPIView

__all__ = [
    UserRegisterAPIView, 
    UserLoginAPIView, 
    GetProfileAPIView,
    UserLogoutAPIView,
    ActivationAPIView,
]