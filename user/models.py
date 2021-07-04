from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from company.models import Company
from util.TimeStampModel import TimeStampModel


class User(TimeStampModel, AbstractUser):
    social_number = models.CharField(max_length=14, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    objects = UserManager()

    def clean(self, *args, **kwargs):
        # add custom validation here
        super(User, self).clean(*args, **kwargs)
        qs_social_number = self.__class__._default_manager.filter(social_number=self.social_number)
        qs_username = self.__class__._default_manager.filter(username=self.username)
        if qs_social_number.exists():
            raise ValidationError(f'User with social_number: {self.social_number} already exists.')
        if qs_username.exists():
            raise ValidationError(f'User with email: {self.email} already exists.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'USER'
        verbose_name = _('users')
        verbose_name_plural = _('user')
