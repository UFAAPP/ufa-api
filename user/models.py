from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from company.models import Company
from util.TimeStampModel import TimeStampModel


class User(TimeStampModel, AbstractUser):
    social_number = models.CharField(max_length=14, unique=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'USER'
        verbose_name = _('users')
        verbose_name_plural = _('user')
