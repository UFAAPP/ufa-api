from django.urls import include, path
from rest_framework.routers import SimpleRouter

from lawsuit import views

router = SimpleRouter()
router.register('', views.LawsuitView)

urlpatterns = [
    path('lawsuits', include(router.urls)),
]
