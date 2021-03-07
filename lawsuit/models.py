from django.db import models
from django.utils.translation import gettext_lazy as _
from client.models import Client
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


class Locker(TimeStampModel):
    class Meta:
        db_table = 'LOCKER'

    number = models.IntegerField()
    full = models.BooleanField()


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
    observation = models.TextField()
    identifier = models.CharField(max_length=30)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)


