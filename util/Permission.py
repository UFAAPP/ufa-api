import jwt
import requests
import json
from uuid import UUID
from django.db.models import Manager, Q
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext

from util.auth import SafeJWTAuthentication


class PermissionMiddleware:

    company_id = None
    user_is_superuser = False
    user_name = None

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        PermissionMiddleware.user_id = None
        PermissionMiddleware.user_is_superuser = False

        user = SafeJWTAuthentication.authenticate(self, request)
        if user:
            self.company_id = user[0].company_id

        return self.get_response(request)


class ModelPermissionManager(Manager):

    def __init__(self, clause_list):
        super().__init__()
        self.clause_list = clause_list

    def get_queryset(self):
        company_id = PermissionMiddleware.company_id

        if PermissionMiddleware.user_is_superuser:
            return super().get_queryset().all()
        elif company_id:
            q = Q()

            for clause in self.clause_list:
                q |= Q(**{clause: company_id})

            return super().get_queryset().filter(q).distinct()
        else:
            return super().get_queryset()