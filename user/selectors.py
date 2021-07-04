from django.core.exceptions import ObjectDoesNotExist

from user.models import User


def find_user_by_username(*, username: str):
    try:
        return User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None


def find_user_by_id(*, id):
    try:
        return User.objects.get(id=id)
    except ObjectDoesNotExist:
        return None
