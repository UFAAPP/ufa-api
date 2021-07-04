from rest_framework.views import APIView

from client.filter import ClientsFilter
from client.serializers import ClientSerializer
from client.services import ClientService
from util.mixins import ApiErrorsMixin
from util.pagination import Pagination


class ClientGetView(ApiErrorsMixin, APIView):
    pagination = Pagination()

    def get(self, request):
        service = ClientService()
        queryset = service.filter_queryset()
        clients = ClientsFilter(request.GET, queryset=queryset)
        page = self.pagination.paginate_queryset(clients.qs, request)
        clients_data = ClientSerializer(page, many=True).data
        return self.pagination.get_paginated_response(clients_data)
