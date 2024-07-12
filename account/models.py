from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(null=True, blank=True, max_length=20, verbose_name="Phone")