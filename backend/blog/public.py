from backend.blog import signals


def publish_blog(blog_id):
    signals.notify_author.send(sender=None, blog_id=blog_id)
