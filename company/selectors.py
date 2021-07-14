from company.models import Company


def find_company_by_document_number(*, document_number: str) -> Company:
    try:
        return Company.objects.get(document_number=document_number)
    except Company.DoesNotExist:
        return None


def find_company_by_id(*, company_id: int) -> Company:
    try:
        return Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return None
