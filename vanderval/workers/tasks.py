from celery import Task
from website.tasks import task_01, task_02, task_03, task_04, task_05
from vanderval.celery import app
from .job_types import JobType
from .customer_types import CustomerType
from website.models import Site


class PrioritizedTask(Task):
    def apply_async(self, args=None, kwargs=None, **options):
        site_id = args[0] if args else kwargs.get('site_id')
        site = Site.objects.get(id=site_id)
        
        customer_type = CustomerType(site.record_capicity)
        priority_queue = CustomerType.get_priority(customer_type)
        
        if priority_queue:
            options['queue'] = priority_queue
        else:
            raise ValueError(f"Invalid customer priority for site {site_id}")
        
        return super().apply_async(args=args, kwargs=kwargs, **options)


@app.task(base=PrioritizedTask, bind=True)
def execute_task(self, site_id: int, job_type: int):
    task_mapping = {
        JobType.VERY_FAST.value: task_01,
        JobType.FAST.value: task_02,
        JobType.MEDIUM.value: task_03,
        JobType.SLOW.value: task_04,
        JobType.VERY_SLOW.value: task_05
    }
    
    task_func = task_mapping.get(job_type)
    if not task_func:
        raise ValueError(f"Invalid job type: {job_type}")
    
    return task_func(site_id)
