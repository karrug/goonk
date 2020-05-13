from django.db import models


class Job(models.Model):
    job_id = models.CharField(max_length=32, unique=True)
    code = models.TextField()
    result = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return self.job_id
