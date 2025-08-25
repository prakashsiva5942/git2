from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.user_list, name="users"),
    path("tasks/", views.task_list, name="tasks"),
    path("reports/", views.reports, name="reports"),
]
