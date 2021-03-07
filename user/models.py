from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

from company.models import Company


class User(AbstractUser):
    social_number = models.CharField(max_length=14, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    objects = UserManager()
