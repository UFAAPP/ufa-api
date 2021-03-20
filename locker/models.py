from django.db import models

from company.models import Company
from util.TimeStampModel import TimeStampModel


class Locker(TimeStampModel):
    class Meta:
        db_table = 'LOCKER'

    number = models.IntegerField()
    full = models.BooleanField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=False)
