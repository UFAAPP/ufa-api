import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from client.models import Client
from company.models import Company
from locker.models import Locker
from util.TimeStampModel import TimeStampModel


class Court(models.TextChoices):
    INFANCIA = 'IN', _('Vara de Infância e Juventude')
    FAZENDA = 'FA', _('Vara da Fazenda Pública')
    CIVEL = 'CI', _('Vara Civel')
    FAMILIA = 'FM', _('Vara de família')
    CRIMINAL = 'CR', _('Vara Criminal')
    ESPECIAL_CRIMINAL = 'ER', _('Juizado Especial Criminal')
    AUXILIARES = 'AU', _('Juízes de Direito Auxiliares')
    ESPECIAL_CIVEL = 'EC', _('Juizado Especial Cível')
    UNICA = 'UN', _('Vara Unica')


class LawsuitStatus(models.TextChoices):
    PROGRESS = 'PROGRESS'
    ARCHIVED = 'ARCHIVED'


class Lawsuit(TimeStampModel):
    class Meta:
        db_table = 'LAWSUIT'

    district = models.CharField(max_length=100)
    court = models.CharField(
        max_length=2,
        choices=Court.choices,
        default=Court.UNICA,
    )
    observation = models.TextField()
    code_number = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    descriptor = models.CharField(max_length=150)
    observation = models.TextField(null=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=False)
    status = models.CharField(
        max_length=10,
        choices=LawsuitStatus.choices,
        default=LawsuitStatus.PROGRESS,
    )
