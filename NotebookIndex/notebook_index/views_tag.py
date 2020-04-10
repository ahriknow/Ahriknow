from rest_framework.response import Response
from rest_framework.views import APIView
from NotebookManage.notebook.models import Tag
from NotebookIndex.notebook_index.serializer import ManyTag


class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.filter()
        data = ManyTag(instance=tags, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
