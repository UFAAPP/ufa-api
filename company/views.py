from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from client.models import Client
from company.models import Company
from lawsuit.models import Locker, Lawsuit


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]


class CompanyTotalSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class CompanyTotalOutputSerializer(serializers.Serializer):
    count_client = serializers.IntegerField()
    count_locker = serializers.IntegerField()
    count_lawsuit = serializers.IntegerField()


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
