from django.urls import path
from apps.payments.views import OrderCreateAPIView

app_name = "payments"

urlpatterns = [
    path("order-create/", OrderCreateAPIView.as_view(), name="order-create")
]