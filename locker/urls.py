from django.urls import include, path
from rest_framework.routers import SimpleRouter

from locker import views

router = SimpleRouter()
router.register('', views.LockerView)

urlpatterns = [
    path('lockers', include(router.urls)),
]
