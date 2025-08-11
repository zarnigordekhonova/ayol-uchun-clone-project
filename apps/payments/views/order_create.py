from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from django.db import transaction

from apps.payments.models import Transaction, Providers, Order
from apps.payments.choices import ProviderChoices, TransactionStatus, OrderStatus
from apps.payments.serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

