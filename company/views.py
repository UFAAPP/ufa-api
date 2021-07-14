from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from client.models import Client
from company.serializers import CompanyTotalSerializer, CompanyTotalOutputSerializer, \
    CompanyCreateApiInputSerializer
from company.services import AddCompany
from lawsuit.models import Lawsuit
from locker.models import Locker
from util.auth import SafeJWTAuthentication
from util.mixins import ApiErrorsMixin
from rest_framework.permissions import IsAuthenticated

# class CompanyView(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanyCreateApiInputSerializer
#     permission_classes = [AllowAny]


class CompanyCreateApi(ApiErrorsMixin, APIView):
    authentication_classes = [SafeJWTAuthentication]
    permission_classes = [IsAuthenticated]


    def __init__(self):
        self.add_company = AddCompany()

    def post(self, request):
        serializer = CompanyCreateApiInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.add_company.add(**serializer.validated_data, user=request.user)

        return Response(status=status.HTTP_201_CREATED)


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
