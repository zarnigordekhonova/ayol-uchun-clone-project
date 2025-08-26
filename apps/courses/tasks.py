from core.celery import app
from django.utils import timezone
from apps.courses.models import Webinar

@app.task()
def set_all_upcoming_live(webinar_id):
    now = timezone.now()
    webinar = Webinar.objects.get(id=webinar_id)
    if webinar.status == "upcoming" and webinar.datetime <= now:
        webinar.status = "live"
        webinar.save()
        print(f"✅ Webinar {webinar.id} is now live!")
