from company.models import Company
from company.selectors import find_company_by_document_number
from user.models import User
from django.core.exceptions import ValidationError


class AddCompany:

    def add(self, *, business_name: str, document_number: str, user: User) -> Company:
        has_company = find_company_by_document_number(document_number=document_number)
        if has_company:
            raise ValidationError('This document number already exists.')

        company = Company.objects.create(business_name=business_name, document_number=document_number)
        user.company = company
        user.save()
        return company
