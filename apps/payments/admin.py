from django.contrib import admin
from django.utils.html import format_html

from apps.payments.models import Order, ProviderCredentials, Providers, Transaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user__username",
        "get_course",
        "get_webinar",
        "status",
        "amount",
        "created_at"
    )
    list_display_links = ("id", "user__username")
    search_fields = ("user__username",)
    ordering = ("-created_at",)

    def get_course(self, obj):
        if obj.course:
            return format_html('<span style="color:green;">{}</span>', obj.course.title)
        print("OBJECT", obj)
        return format_html('<span style="color:red;">❌</span>')
    get_course.short_description = "Course"


    def get_webinar(self, obj):
        if obj.webinar:
            return format_html('<span style="color:green;">{}</span>', obj.webinar.title)
        return format_html('<span style="color:red;">❌</span>')
    get_webinar.short_description = "Webinar"



@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "status", "amount", "created_at")
    list_display_links = ("id", "order")
    search_fields = ("order__user__username",)
    ordering = ("-created_at",)


@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "key")
    list_display_links = ("id", "name")
    search_fields = ("name", "key")
    ordering = ("-created_at",)


@admin.register(ProviderCredentials)
class ProviderCredentialsAdmin(admin.ModelAdmin):
    list_display = ("id", "provider", "key")
    list_display_links = ("id", "provider")
    search_fields = ("provider__name", "key")
    ordering = ("-created_at",)