from client.models import Client
from company.models import Company


def find_client_by_social_number(*, social_number: str) -> Client:
    try:
        return Client.objects.get(social_number=social_number)
    except Client.DoesNotExist:
        return None


def find_clients_by_company(*, company: Company):
    return Client.objects.filter(company=company)
