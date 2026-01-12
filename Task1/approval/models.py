

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"


class Task(models.Model):
    STATUS_CHOICES = [
        ('ASSIGNED', 'On Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ASSIGNED')
    parent_task = models.ForeignKey("self", null=True, blank=True,
                                    on_delete=models.CASCADE, related_name="child_tasks")
    created_at = models.DateTimeField(auto_now_add=True)

    def display_status(self):
        return "onProgress" if self.status == "ASSIGNED" else "Completed"

    def __str__(self):
        return f"{self.title} - {self.department.name} - {self.status}"
