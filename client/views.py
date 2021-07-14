from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from client.filter import ClientsFilter
from client.serializers import ClientCreateApiInputOutputSerializer
from client.services import ClientService, AddClient, LoadClientsByCompany
from util.auth import SafeJWTAuthentication
from util.mixins import ApiErrorsMixin
from util.pagination import Pagination


class ClientListCreateApi(ApiErrorsMixin, APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.add_client = AddClient()
        self.load_clients_by_company = LoadClientsByCompany()

    def post(self, request):
        serializer = ClientCreateApiInputOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        client = self.add_client.add(**serializer.validated_data, user=request.user)
        serializer = ClientCreateApiInputOutputSerializer(instance=client)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        clients = self.load_clients_by_company.load(company=request.user.company)

        serializer = ClientCreateApiInputOutputSerializer(instance=clients, many=True)

        return Response(data=serializer.data)
