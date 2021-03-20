from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyTotalSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class CompanyTotalOutputSerializer(serializers.Serializer):
    count_client = serializers.IntegerField()
    count_locker = serializers.IntegerField()
    count_lawsuit = serializers.IntegerField()
