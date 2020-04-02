from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookManage.notebook.models import Book
from NotebookManage.notebook.serializer import OneBook, ManyBook


class BookView(APIView):
    def get(self, request, id=None):
        if id:
            if book := Book.objects.filter(pk=id, user=request.u).first():
                data = OneBook(instance=book, many=False).data
                return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        else:
            books = Book.objects.filter(user=request.u)
            data = ManyBook(instance=books, many=True).data
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            book = Book(name=request.data['name'], describe=request.data['describe'], image=request.data['image'],
                        public=request.data['public'])
            book.user = request.u
            book.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if book := Book.objects.filter(pk=id).first():
            data = request.data
            if name := data.get('name'):
                book.name = name
            if describe := data.get('describe'):
                book.describe = describe
            if image := data.get('image'):
                book.image = image
            if public := data.get('public'):
                book.public = public
            book.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if book := Book.objects.filter(pk=id).first():
            book.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
