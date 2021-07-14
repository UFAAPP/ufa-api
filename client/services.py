from client.models import Client
from django.core.exceptions import ValidationError

from client.selectors import find_client_by_social_number, find_clients_by_company
from company.models import Company
from user.models import User


class ClientService:
    def get_clients(self):
        pass

    @staticmethod
    def filter_queryset():
        query = Client.objects.all()
        query = query.order_by('-created')
        return query


class AddClient:

    def add(self, *, name: str, social_number: str, email: str, phone: str, whatsapp: str, observation: str, user: User) -> Client:
        has_client = find_client_by_social_number(social_number=social_number)
        if has_client:
            raise ValidationError('This social number already exists.')

        client = Client.objects.create(
            name=name,
            social_number=social_number,
            email=email,
            phone=phone,
            whatsapp=whatsapp,
            observation=observation,
            company=user.company
        )
        return client


class LoadClientsByCompany:

    def load(self, *, company: Company):
        return find_clients_by_company(company=company)
