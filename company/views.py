from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from client.models import Client
from company.permissions import isCompanyOwner
from company.serializers import CompanyTotalSerializer, CompanyTotalOutputSerializer, CompanySerializer
from company.services import AddCompany, LoadCompanyById
from lawsuit.models import Lawsuit
from locker.models import Locker
from util.auth import SafeJWTAuthentication
from util.mixins import ApiErrorsMixin
from rest_framework.permissions import IsAuthenticated


class CompanyCreateApi(ApiErrorsMixin, APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self):
        self.add_company = AddCompany()

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.add_company.add(**serializer.validated_data, user=request.user)

        return Response(status=status.HTTP_201_CREATED)


class CompanyDetailApi(ApiErrorsMixin, APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated, isCompanyOwner]

    def __init__(self):
        self.load_company_by_id = LoadCompanyById()

    def get(self, request, company_id):
        company = self.load_company_by_id.load(company_id=company_id)
        serializer = CompanySerializer(instance=company)
        return Response(data=serializer.data)


class CompanyTotalView(APIView):
    serializer_class = CompanyTotalSerializer

    @swagger_auto_schema(request_body=CompanyTotalSerializer,
                         responses={200: CompanyTotalOutputSerializer})
    def post(self, request):
        company_id = request.data.get('company_id')
        count_client = Client.objects.filter(company=company_id).count()
        count_locker = Locker.objects.filter(company=company_id).count()
        count_lawsuit = Lawsuit.objects.filter(company=company_id).count()
        rsp = Response()
        rsp.data = {
            'count_client': count_client,
            'count_locker': count_locker,
            'count_lawsuit': count_lawsuit
        }
        return rsp
