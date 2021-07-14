from django.urls import path

from user.views import UserCreateApi

app_name = 'users'

urlpatterns = [
    path(app_name, UserCreateApi.as_view()),
]
