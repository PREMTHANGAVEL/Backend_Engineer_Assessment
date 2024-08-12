from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=255)
    schedule_interval = models.TextField(blank=True, null=True)
    last_run_time = models.DateTimeField(null=True, blank=True)
    next_run_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
