
from django.urls import path

from apps.common.views import FrontendTranslationView, VersionHistoryView
from apps.common.homepage import home

app_name = "common"

urlpatterns = [
    path("", home, name="home"),
    path(
        "FrontendTranslations/",
        FrontendTranslationView.as_view(),
        name="frontend-translations",
    ),
    path("VersionHistory/", VersionHistoryView.as_view(), name="version-history"),
]