from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method
from rest_framework import serializers, viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from company.views import CompanySerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserCompanySerializer(serializers.ModelSerializer):

    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company']


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersCompanyView(viewsets.ViewSet):
    serializer_class = UserCompanySerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=UserCompanySerializer)
    def create(self, request):
        company = CompanySerializer(request.data['company'], self).create()
        user = 'teste'

