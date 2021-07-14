from django.urls import include, path

from company.views import CompanyCreateApi, CompanyTotalView

urlpatterns = [
    path('companies', CompanyCreateApi.as_view()),
    path('companies/total', CompanyTotalView.as_view()),
]
