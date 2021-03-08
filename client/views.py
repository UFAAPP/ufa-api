from rest_framework import serializers, viewsets
from client.models import Client
from util.Permission import ModelPermissionManager


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
