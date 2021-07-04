from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.authtoken.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.serializers import AuthInputSerializer, AuthOutputSerializer, AuthRefreshOutputSerializer, \
    AuthRefreshInputSerializer
from authentication.services import AuthenticationService
from util.mixins import ApiErrorsMixin


class AuthView(APIView, ApiErrorsMixin):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        responses={400: 'Bad request', 200: AuthOutputSerializer},
        request_body=AuthInputSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = AuthInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthenticationService()
        response = service.get_token(**serializer.validated_data)
        return Response(data=AuthOutputSerializer(response).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AuthRefreshInputSerializer,
                         responses={200: AuthRefreshOutputSerializer(many=False)})
    def put(self, request):
        serializer = AuthRefreshInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthenticationService()
        response = service.update_token(**serializer.validated_data)
        return Response(data=AuthRefreshOutputSerializer(response).data, status=status.HTTP_200_OK)


class AuthLogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    get_response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING)})

    @swagger_auto_schema(responses={
        500: get_response_schema,
        204: get_response_schema
    })
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return HttpResponse(b'{"message": "Logout successeful"}',
                                content_type='application/json',
                                status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return HttpResponse(b'{"message": "Problems for logout"}',
                                content_type='application/json',
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
