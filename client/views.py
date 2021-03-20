from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.utils import json

from client.models import Client
from client.serializers import ClientSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.filter()
    serializer_class = ClientSerializer

    def list(self, request, *args, **kwargs):
        queryset = Client.objects.filter()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return HttpResponse(json.dumps(serializer.data),
                            content_type='application/json',
                            status=status.HTTP_200_OK)
