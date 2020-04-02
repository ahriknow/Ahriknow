from rest_framework.response import Response
from rest_framework.views import APIView

from NotebookManage.notebook.models import Book, Catalog
from NotebookManage.notebook.serializer import ManyCatalog


class CatalogView(APIView):
    def get(self, request, id=None):
        catalog = Catalog.objects.filter(book=Book.objects.filter(pk=id).first())
        data = ManyCatalog(instance=catalog, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request, id=None):
        try:
            catalog = Catalog(name=request.data['name'])
            catalog.book = Book.objects.filter(pk=id).first()
            if request.data.get('parent'):
                catalog.parent = Catalog.objects.filter(pk=request.data['parent']).first()
            catalog.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if catalog := Catalog.objects.filter(pk=id).first():
            if name := request.data.get('name'):
                catalog.name = name
            catalog.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if catalog := Catalog.objects.filter(pk=id).first():
            catalog.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
