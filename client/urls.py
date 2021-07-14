from django.urls import path

from client.views import ClientListCreateApi

app_name = 'clients'

urlpatterns = [
    # path(app_name, ClientGetView.as_view()),
    path(app_name, ClientListCreateApi.as_view()),

]
