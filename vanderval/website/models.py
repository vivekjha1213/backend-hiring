from django.db import models


# Create your models here.
class Site(models.Model):
    RECORD_CAPACITY_LOW = 1  # user records between 500-10000
    RECORD_CAPACITY_MEDIUM = 2  # user records between 10000-50000
    RECORD_CAPACITY_HIGH = 3  # user records between 50000-200000

    RECORD_CAPACITY_CHOICES = (
        (RECORD_CAPACITY_LOW, "Low"),
        (RECORD_CAPACITY_MEDIUM, "Medium"),
        (RECORD_CAPACITY_HIGH, "High"),
    )

    name = models.CharField(max_length=100)
    domain = models.URLField()
    url = models.URLField()
    description = models.TextField()
    record_capicity = models.IntegerField(choices=RECORD_CAPACITY_CHOICES)


# you can choose to reuse the User model from django.contrib.auth.models
class UserRecords(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    dob = models.DateField
    is_active = models.BooleanField(default=True)  # do not count for active records if false

class TaskLog(models.Model):
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure')])
    result = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task_name} - {self.status}"