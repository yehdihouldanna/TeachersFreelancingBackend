from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination , CursorPagination
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 30
    last_page_string = "last"

