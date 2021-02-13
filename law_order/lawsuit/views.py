from rest_framework import serializers, viewsets

from lawsuit.models import Lawsuit, Locker


class LockerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Locker
        fields = '__all__'


class LockerView(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer


class LawsuitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lawsuit
        fields = '__all__'


class LawsuitView(viewsets.ModelViewSet):
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer
