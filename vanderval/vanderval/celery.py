# vanderval/vanderval/celery.py
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vanderval.settings')

# Create the Celery app
app = Celery('vanderval',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()