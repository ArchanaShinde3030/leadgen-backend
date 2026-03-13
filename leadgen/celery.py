
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leadgen.settings")

app = Celery("leadgen")
app.config_from_object("django.conf:settings", namespace="CELERY")

# ← This line is REQUIRED to discover tasks in all apps listed in INSTALLED_APPS
app.autodiscover_tasks()