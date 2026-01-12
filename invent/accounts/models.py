from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES=(
        ("ADMIN","Admin"),("BILLING","Billing Staff"),("ACCOUNTANT","Accountant"),)
    
    
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="BILLING")

    def __str__(self):
        return self.username