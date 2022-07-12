from django.db import models
from django.urls import reverse
from django.utils import timezone


class TodoTask(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return f'Title: {self.title},\nDetails: {self.details}'

    def get_absolute_url(self):
        return reverse('page-todo-detail', kwargs={'pk': self.pk})
