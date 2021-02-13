from django.db import models

from company.models import Company


class User(models.Model):
    social_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)