from django.urls import path

from .views import AuthView, AuthLogoutView

app_name = 'auth'


urlpatterns = [
    path(app_name, AuthView.as_view()),
    path(f'{app_name}/logout', AuthLogoutView.as_view()),
]
