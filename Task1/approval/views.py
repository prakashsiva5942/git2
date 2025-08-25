from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Task


def user_list(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


def task_list(request):
    tasks = Task.objects.all().order_by("id")
    return render(request, "tasks.html", {"tasks": tasks})


def reports(request):
    tasks = Task.objects.all().order_by("id")
    return render(request, "report.html", {"tasks": tasks})

# Create your views here.

