"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="UFA API",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="domvcelos@gmail.com"),
        license=openapi.License(name="BSD License"),
        url='/v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),


    # API PATHS
    path('v1/', include('user.urls', namespace='users')),
    # path('companies/', include('company.urls')),
    path('v1/', include('client.urls', namespace='clients')),
    path('v1/', include('authentication.urls', namespace='authentication')),
    # path('lawsuit/', include('lawsuit.urls')),
    # path('locker/', include('locker.urls')),
]
