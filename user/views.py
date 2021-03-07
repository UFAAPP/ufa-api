from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets, permissions
from rest_framework.views import APIView

from company.views import CompanySerializer
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from util.auth import generate_access_token, generate_refresh_token


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
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company']


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username']


class UsersCompanyView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: UserCompanySerializer(many=False)})
    def post(self, request):
        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()
        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = User.objects.filter(social_number=username) | User.objects.filter(email=username)
        user = user.first()
        if user is None:
            raise exceptions.AuthenticationFailed('user not found or wrong password')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('user not found or wrong password')

        serialized_user = UserCompanySerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response
