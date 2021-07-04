from rest_framework import serializers

from client.models import Client
from lawsuit.models import Lawsuit


class LawsuitUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawsuit
        fields = '__all__'
        depth = 1


class ClientSerializer(serializers.ModelSerializer):
    lawsuits = LawsuitUnrelatedSerializer(source='lawsuit_set', many=True, required=False)

    class Meta:
        model = Client
        fields = '__all__'
