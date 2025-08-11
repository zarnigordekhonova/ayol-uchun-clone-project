from celery import shared_task
from django.utils import timezone
from apps.courses.models import Webinar

@shared_task(name="set_all_upcoming_live")
def set_all_upcoming_live():
    now = timezone.now()
    webinars = Webinar.objects.filter(status="upcoming", datetime__lte=now)
    for webinar in webinars:
        webinar.status = "live"
        webinar.save()
        print(f"✅ Webinar {webinar.id} is now live!")
