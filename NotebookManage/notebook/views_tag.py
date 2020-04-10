from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookManage.notebook.models import Tag
from NotebookManage.notebook.serializer import ManyTag


class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.filter()
        data = ManyTag(instance=tags, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            tag = Tag(name=request.data['name'])
            tag.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def delete(self, request, id=None):
        if tag := Tag.objects.filter(pk=id).first():
            tag.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
