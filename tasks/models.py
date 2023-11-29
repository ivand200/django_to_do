from django.db import models
from django.conf import settings
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Job(models.Model):
    task = models.ForeignKey(Task, related_name="jobs", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    done_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
