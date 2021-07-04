from django.urls import path

from client.views import ClientGetView

app_name = 'clients'

urlpatterns = [
    path(app_name, ClientGetView.as_view()),
]
