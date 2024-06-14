from django.dispatch import receiver
from blog import signals


@receiver(signals.notify_author)
def send_mail_to_author(sender, blog_id, **kwargs):
    print('wysyłanie maila do autora, że jego blog jest opublikowany', blog_id, kwargs)
