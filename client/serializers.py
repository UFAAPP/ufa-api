from rest_framework import serializers

from client.models import Client
from lawsuit.models import Lawsuit


class LawsuitUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawsuit
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    lawsuits = LawsuitUnrelatedSerializer(source='lawsuit_set', many=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'
