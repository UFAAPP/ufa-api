from rest_framework import serializers

from lawsuit.models import Lawsuit


class LawsuitPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawsuit
        fields = '__all__'


class LawsuitGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawsuit
        fields = '__all__'
        depth = 1
