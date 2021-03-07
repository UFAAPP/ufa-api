from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from company import views

router = SimpleRouter()
router.register('', views.CompanyView)


urlpatterns = [
    path('', include(router.urls)),
    url(r'^total', views.CompanyTotalView.as_view()),
]