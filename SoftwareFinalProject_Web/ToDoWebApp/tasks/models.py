from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    due_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.ManyToManyField(User, related_name='assignments')

    def __str__(self):
        return self.name