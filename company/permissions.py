from rest_framework.permissions import BasePermission


class isCompanyOwner(BasePermission):
    message = 'This user is not owner of this company.'

    def has_permission(self, request, view):
        company_id = view.kwargs.get('company_id')
        return bool(request.user.company and request.user.company.id == company_id)
