from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookManage.notebook.models import Catalog, Content
from NotebookManage.notebook.serializer import OneContent


class ContentView(APIView):
    def get(self, request, id=None):
        if catalog := Catalog.objects.filter(pk=id).first():
            content = Content.objects.filter(catalog=catalog).first()
            if not content:
                content = Content(content='## New Note!', catalog=catalog)
                content.save()
            data = OneContent(instance=content, many=False).data
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
        return Response({'code': 400, 'msg': "The 'catalog' does not exist!", 'data': None})

    def put(self, request, id=None):
        try:
            if content := Content.objects.filter(pk=id).first():
                if c := request.data.get('content'):
                    content.content = c
                content.save()
                return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})
