import logging

from backend.config.celery import task

logger = logging.getLogger('my_logger')


@task(bind=True)
def send_email_to_followers(self, author_id, blog_id):
    logger.log(logging.INFO, f'Wysyłam mail do obserwujących autora {author_id} dla bloga {blog_id}')
