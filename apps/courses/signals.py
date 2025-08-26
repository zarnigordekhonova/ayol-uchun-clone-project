from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete

from apps.courses.models import Webinar
from apps.courses.models import Course, Comment
from apps.courses.tasks import set_all_upcoming_live


@receiver(post_save, sender=Webinar)
def schedule_webinar_live(sender, instance, created, **kwargs):
    if created and instance.status == "upcoming":
        set_all_upcoming_live.apply_async(
            args=[instance.id],
            eta=instance.datetime
        )


def update_course_rating(course):
    """
    This function gets all the rating for the given course from comments model's rating field,
    calculates/updates the rating according to the rating given by users.
    """
    result = Comment.objects.filter(course=course).aggregate(
        avg=Avg("rating")
    )
    avg_rating = result['avg'] or 0
    course.rating = avg_rating
    course.save(update_fields=['rating'])


def update_webinar_rating(webinar):
    """
    This function gets all the rating for the given webinar from comments model's rating field,
    calculates/updates the rating according to the rating given by users.
    """
    result = Comment.objects.filter(webinar=webinar).aggregate(
        avg=Avg("rating")
    )
    avg_rating = result['avg'] or 0
    webinar.rating = avg_rating
    webinar.save(update_fields=["rating"])


# Signals for updating Comment model's rating
@receiver(post_save, sender=Comment)
def course_comment_saved(sender, instance, **kwargs):
    if instance.course:
        update_course_rating(instance.course)
    if instance.webinar:
        update_webinar_rating(instance.webinar)


@receiver(post_delete, sender=Comment)
def course_comment_deleted(sender, instance, **kwargs):
    if instance.course:
        update_course_rating(instance.course)
    if instance.webinar:
        update_webinar_rating(instance.webinar)


