from django_filters import FilterSet, CharFilter

from client.models import Client


class ClientsFilter(FilterSet):
    social_number = CharFilter('social_number', lookup_expr='iexact')
    name = CharFilter('name', lookup_expr='icontains')
    email = CharFilter('email', lookup_expr='iexact')
    company = CharFilter('company', lookup_expr='iexact')
    active = CharFilter('active', lookup_expr='iexact')

    class Meta:
        model = Client
        fields = ['social_number',
                  'name',
                  'email',
                  'company',
                  'active']
