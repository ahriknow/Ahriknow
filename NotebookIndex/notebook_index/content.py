from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookIndex.notebook_index.serializer import OneContent
from NotebookManage.notebook.models import Catalog, Content


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
