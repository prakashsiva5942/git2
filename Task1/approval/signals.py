from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Department


@receiver(post_save, sender=Task)
def create_dept2_task(sender, instance, **kwargs):
    """
    When a Dept1 task is marked completed,
    auto-create a Dept2 task with same title/description.
    """
    if instance.department.name == "DEPT 1" and instance.status == "COMPLETED":
        dept2 = Department.objects.get(name="DEPT 2")

        # Prevent duplicate Dept2 task
        if not Task.objects.filter(parent_task=instance, department=dept2).exists():
            Task.objects.create(
                title=instance.title,
                description=instance.description,
                department=dept2,
                parent_task=instance
            )
