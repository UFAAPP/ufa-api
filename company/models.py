from django.db import models


class Company(models.Model):
    social_number = models.CharField(max_length=14)
    name = models.CharField(max_length=100)