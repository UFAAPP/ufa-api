from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from collections import OrderedDict


class Pagination(LimitOffsetPagination):
    default_limit = 100

    def get_paginated_response(self, data, data_totalizer=None):
        data_result = OrderedDict([
            ('count', self.count),
            ('limit', self.limit),
            ('offset', self.offset),
            ('results', data)
        ])
        if data_totalizer is not None:
            data_result.update(data_totalizer)
        return Response(data_result)


def paginate_array(items: list, limit=1):
    """
    return: Array containing another arrays with the length defined by limit parameter
    """
    return [items[i:i + limit] for i in range(0, len(items), limit)]
