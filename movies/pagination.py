from rest_framework.pagination import PageNumberPagination

class ResultsPagination(PageNumberPagination):
    page_size = 10 
    # Parámetro a especificar en la url ?page=2 (second page)
    page_query_param = 'page'