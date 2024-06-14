from celery import Celery

celery_setting_value = "config.settings"

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

task = app.task


@app.task(bind=True)
def debug_task(self, data):
    print(data)
