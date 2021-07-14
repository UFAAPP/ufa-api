from django.urls import include, path

from company.views import CompanyCreateApi, CompanyTotalView, CompanyDetailApi

urlpatterns = [
    path('companies', CompanyCreateApi.as_view()),
    path('companies/<int:company_id>', CompanyDetailApi.as_view()),
    path('companies/total', CompanyTotalView.as_view()),
]
