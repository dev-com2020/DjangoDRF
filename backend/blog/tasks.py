from backend.config.celery import task


@task(bind=True)
def send_email_to_followers(self, author_id, blog_id):
    print(f'Wysyłam mail do obserwujących autora {author_id} dla bloga {blog_id}')
