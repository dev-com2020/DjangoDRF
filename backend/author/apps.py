from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    name = "author"

    def ready(self):
        from author import receivers
