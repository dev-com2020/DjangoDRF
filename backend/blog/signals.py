# from django import dispatch
#
# notify_author = dispatch.Signal()
#

from django.db.models.signals import post_save
from django.dispatch import receiver
from blog import models


@receiver(post_save, sender=models.Blog)
def blog_post_saved(sender, instance, created, **kwargs):
    if created:
        print(f'Stworzono nowy blog: {instance.title} ')
    else:
        print("Czy to jest widoczne?")
