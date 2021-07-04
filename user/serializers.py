from rest_framework import serializers

from company.views import CompanySerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserInputSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    social_number = serializers.CharField(required=True, max_length=11, min_length=11)
    password = serializers.CharField(required=True)


class UserCompanySerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company']
        extra_kwargs = {
            'password': {'write_only': True}
        }
