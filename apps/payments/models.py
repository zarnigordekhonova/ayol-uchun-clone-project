import datetime

from django.db import models, transaction
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.payments.choices import OrderStatus, TransactionStatus, ProviderChoices


class Order(BaseModel):
    user =  models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="orders",
        verbose_name=_("CustomUser"),
        null=True,
        blank=True
    )

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.SET_NULL,
        related_name="orders",
        verbose_name=_("Course"),
        null=True,
        blank=True
    )

    webinar = models.ForeignKey(
        "courses.Webinar",
        on_delete=models.SET_NULL,
        related_name="orders",
        verbose_name=_("Webinar"),
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Amount")
    )

    status = models.CharField(
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name=_("Status")
    )

    is_paid = models.BooleanField(default=False, verbose_name=_("Is Paid"))
    
    def __str__(self):
        return f"Order: {self.id}"
        
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class Transaction(BaseModel):
    order =  models.ForeignKey(
        "payments.Order", on_delete=models.CASCADE, verbose_name=_("orders")
    )
    
    provider = models.ForeignKey(
        "payments.Providers", on_delete=models.CASCADE, verbose_name=_("Provider")
    )

    status = models.CharField(
        max_length=10,
        choices=TransactionStatus.choices,
        default=TransactionStatus.PENDING,
        verbose_name= _("Status")
    )

    paid_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Paid at"))
    cancelled_at =  models.DateTimeField(null=True, blank=True, verbose_name=_("Cancelled at"))
    remote_id = models.CharField(max_length=512, null=True, blank=True, verbose_name=_("Remote Transaction ID"))
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Amount"))
    extra = models.JSONField(null=True, blank=True, verbose_name=_("Extra data"))

    def __str__(self):
        return f"Transaction: {self.id}"
    
    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    # @property 



class Providers(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), choices=ProviderChoices.choices)
    key = models.CharField(max_length=255, verbose_name=_("Key"))

    def __str__(self):
        return f"Provider: {self.name}"
    
    class Meta:
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")


class ProviderCredentials(BaseModel):
    provider = models.ForeignKey("payments.Providers", on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    key_description = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            "provider",
            "key"
        )
        verbose_name = _("Provider Credential")
        verbose_name_plural = _("Provider Credentials")

    def __str__(self):
        return f"{self.provider} : {self.key}"


