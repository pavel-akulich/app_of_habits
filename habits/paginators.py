from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Paginator for habits.

    Attributes:
        page_size (int): The number of habits to include on each page.
        page_size_query_param (str): The query parameter for specifying the page size.
        max_page_size (int): The maximum allowed page size.
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
