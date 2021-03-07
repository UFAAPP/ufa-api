from django.urls import include, path
from rest_framework.routers import SimpleRouter

from lawsuit import views

router = SimpleRouter()
router.register('lawsuit', views.LawsuitView)
router.register('locker', views.LockerView)

urlpatterns = [
    path('', include(router.urls)),
]