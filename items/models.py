from django.db import models


class items(models.Model):
    task_name = models.TextField(max_length=100)