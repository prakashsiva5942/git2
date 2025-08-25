from django.contrib import admin
from .models import Department, Profile, Task
from django import forms
from django.contrib.auth.models import User


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and self.instance.department:
            self.fields["assigned_to"].queryset = User.objects.filter(
                profile__department=self.instance.department
            )
        elif "department" in self.data:
            try:
                dept_id = int(self.data.get("department"))
                self.fields["assigned_to"].queryset = User.objects.filter(profile__department_id=dept_id)
            except (ValueError, TypeError):
                self.fields["assigned_to"].queryset = User.objects.none()
        else:
            self.fields["assigned_to"].queryset = User.objects.none()


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = ("title", "department", "status", "assigned_to", "created_at")
    list_filter = ("department", "status")
    search_fields = ("title", "description")


admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(Task, TaskAdmin)

# Register your models here.
