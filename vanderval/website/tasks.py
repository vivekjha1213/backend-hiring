from django.utils import timezone
import logging
from time import sleep
from celery.signals import task_prerun, task_postrun, task_failure
from celery.result import AsyncResult  # Import AsyncResult to get task results
from .models import TaskLog, Site, UserRecords

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@task_prerun.connect
def task_prerun_handler(task_id, task, args, kwargs, **extras):
    TaskLog.objects.create(
        task_name=task.name,
        status='STARTED',
        result="",
    )

@task_postrun.connect
def task_postrun_handler(task_id, task, args, kwargs, **extras):
    task_log = TaskLog.objects.filter(task_name=task.name, status='STARTED').last()
    if task_log:
        task_log.status = 'SUCCESS'
        task_log.finished_at = timezone.now()

        # Use AsyncResult to get the task result
        result = AsyncResult(task_id).result
        task_log.result = str(result)  # Convert the result to a string
        task_log.save()

@task_failure.connect
def task_failure_handler(task_id, task, args, kwargs, exception, **extras):
    task_log = TaskLog.objects.filter(task_name=task.name, status='STARTED').last()
    if task_log:
        task_log.status = 'FAILURE'
        task_log.finished_at = timezone.now()
        task_log.error_message = str(exception)
        task_log.save()



def task_01(site_id: int):
    TIME_MULTIPLIER = 0.001 # very fast execution per record
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 01: {} processed".format(record.name))
    return True


def task_02(site_id: int):
    TIME_MULTIPLIER = 0.01
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 02: {} processed".format(record.name))
    return True


def task_03(site_id: int):
    TIME_MULTIPLIER = 0.1
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 03: {} processed".format(record.name))
    return True


def task_04(site_id: int):
    TIME_MULTIPLIER = 1
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 04: {} processed".format(record.name))
    return True


def task_05(site_id: int):
    TIME_MULTIPLIER = 10
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 05: {} processed".format(record.name))
    return True
