from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class ProductTypeChoices(TextChoices):
    COURSE = "course", "Course"
    WEBINAR = "webinar", "Webinar"


class WebinarStatusChoices(TextChoices):
    UPCOMING = ("upcoming", _("Upcoming"))
    LiVE = ("live", _("Live"))
    FINISHED = ("finished", _("Finished"))
