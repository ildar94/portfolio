from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



class MyCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),

            },

            'page_size': len(data),
            'total_count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'results': data

        })
