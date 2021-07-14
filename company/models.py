from django.db import models


class Company(models.Model):

    class Meta:
        db_table = 'COMPANY'

    document_number = models.CharField(max_length=14)
    business_name = models.CharField(max_length=100)

