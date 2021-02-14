from django.urls import include, path
from rest_framework.routers import SimpleRouter

from user import views

router = SimpleRouter()
router.register('', views.UsersView)

urlpatterns = [
    path('', include(router.urls)),
]