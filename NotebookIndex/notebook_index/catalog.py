from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookIndex.notebook_index.serializer import ManyCatalog
from NotebookManage.notebook.models import Book, Catalog


class CatalogView(APIView):
    def get(self, request, id=None):
        catalog = Catalog.objects.filter(book=Book.objects.filter(pk=id).first())
        data = ManyCatalog(instance=catalog, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
