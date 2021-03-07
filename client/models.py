from django.db import models
from django.db.models import DO_NOTHING

from company.models import Company


class Client(models.Model):

    class Meta:
        db_table = 'CLIENT'

    social_number = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    observation = models.TextField()
    phone = models.CharField(max_length=13) #5548999999999
    whatsapp = models.CharField(max_length=13) #5548999999999
    company = models.ForeignKey(Company, on_delete=DO_NOTHING, null=False)