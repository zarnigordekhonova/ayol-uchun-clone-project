from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.courses.models import Webinar
from apps.courses.tasks import set_webinar_live

@receiver(post_save, sender=Webinar)
def schedule_webinar_live(sender, instance, created, **kwargs):
    if created and instance.status == "upcoming":
        set_webinar_live.apply_async(
            args=[instance.id],
            eta=instance.datetime
        )
