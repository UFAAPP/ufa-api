from rest_framework import serializers, viewsets, response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from client.models import Client
from company.models import Company
from lawsuit.models import Locker, Lawsuit
from user.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]


class CompanyTotalView(APIView):

    def post(self, request):
        company_id = 1
        count_client = Client.objects.filter(company=company_id).count()
        count_locker = Locker.objects.filter(company=company_id).count()
        count_lawsuit = Lawsuit.objects.filter(company=company_id).count()
        response.data = {
            'count_client': count_client,
            'count_locker': count_locker,
            'count_lawsuit': count_lawsuit
        }
        return response