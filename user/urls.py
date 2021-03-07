from django.urls import include, path
from rest_framework.routers import SimpleRouter

from user import views

router = SimpleRouter()
router.register('users', views.UsersView)
router.register('users_company', views.UsersCompanyView, 'user_company')

urlpatterns = [
    path('', include(router.urls)),
]