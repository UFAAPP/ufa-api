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

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserCompanySerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username']


class LoginRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)
