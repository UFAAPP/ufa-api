from django.db import models


class Client(models.Model):
    social_number = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    observation = models.TextField()
    phone = models.CharField(max_length=13) #5548999999999
    whatsapp = models.CharField(max_length=13) #5548999999999