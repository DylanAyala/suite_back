from django.db import models 
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True, db_index=True)
    phone = models.CharField(max_length=12, null=False,
                             unique=True, db_index=True)
    lenguage = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(upload_to="avatars", null=True)
