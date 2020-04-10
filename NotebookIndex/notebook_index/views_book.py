from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookManage.notebook.models import Book, Tag
from NotebookIndex.notebook_index.serializer import ManyBook, PageBook


class BookView(APIView):
    def get(self, request):
        where = request.query_params.get('search')
        if t := request.query_params.get('select'):
            books = []
            ids= []
            for i in Tag.objects.filter(id__in=t.split(',')):
                for j in ManyBook(instance=i.book_set.filter(Q(public=True) & Q(name__icontains=where)),
                                  many=True).data:
                    if j['id'] not in ids:
                        books.append(j)
                        ids.append(j['id'])
            return Response({'results': books, 'next': None})
        if where:
            books = Book.objects.filter(Q(public=True) & Q(name__icontains=where))
            return Response({'results': ManyBook(instance=books, many=True).data, 'next': None})
        books = Book.objects.filter(public=True)
        pg = PageBook()
        pgs = pg.paginate_queryset(queryset=books, request=request, view=self)
        data = ManyBook(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res
