from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class PriorityLevel(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    reporter= models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    priority = models.ForeignKey(
        PriorityLevel,
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.summary
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])