from django.urls import include, path
from rest_framework.routers import SimpleRouter

from client import views

router = SimpleRouter()
router.register('', views.ClientView)

urlpatterns = [
    path('', include(router.urls)),
]