from rest_framework import serializers

from locker.models import Locker


class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'
