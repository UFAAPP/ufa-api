from client.models import Client


class ClientService:
    def get_clients(self):
        pass

    @staticmethod
    def filter_queryset():
        query = Client.objects.all()
        query = query.order_by('-created')
        return query
