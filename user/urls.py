from django.urls import path

from user.views import UsersView

app_name = 'users'

urlpatterns = [
    path(app_name, UsersView.as_view()),
]
