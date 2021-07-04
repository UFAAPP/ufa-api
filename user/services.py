from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from user.models import User


class UserService:
    @staticmethod
    def create_user(*, first_name: str, last_name: str, email: str, social_number: str, password: str) -> User:
        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                            is_active=True, social_number=social_number,
                                            username=email, company=None, password=password)
        except IntegrityError:
            raise ValidationError(f'User with email: {email} already exists.')
        return user
