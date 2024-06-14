from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    name = "author"

    def ready(self):
        import author.receivers
