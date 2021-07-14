from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from company.models import Company
from util.TimeStampModel import TimeStampModel


class User(TimeStampModel, AbstractUser):
    social_number = models.CharField(max_length=14, unique=True)

    class Meta:
        db_table = 'USER'
        verbose_name = _('users')
        verbose_name_plural = _('user')
