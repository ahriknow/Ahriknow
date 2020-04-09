from django.db.models import Q
from rest_framework.views import APIView
from NotebookManage.notebook.models import Book
from NotebookIndex.notebook_index.serializer import ManyBook, PageBook


class BookView(APIView):
    def get(self, request):
        if where := request.query_params.get('search'):
            books = Book.objects.filter(Q(public=True) & Q(name__icontains=where))
        else:
            books = Book.objects.filter(public=True)
        pg = PageBook()
        pgs = pg.paginate_queryset(queryset=books, request=request, view=self)
        data = ManyBook(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res
