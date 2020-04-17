from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Tag
from BlogManage.blog.serializer import ManyTag, OneTag


class TagView(APIView):
    def get(self, request, id=None):
        tag = Tag.objects.filter(parent=id)
        data = ManyTag(instance=tag, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            p = None
            w = request.data['weight']
            if p:
                w = 1001
            if t := Tag.objects.filter(pk=request.data.get('parent')).first():
                p = t
            tag = Tag(name=request.data['name'], weight=w, parent=p)
            tag.save()
            data = OneTag(instance=tag, many=False).data
            return Response({'code': 200, 'msg': 'Create successful!', 'data': data})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if tag := Tag.objects.filter(pk=id).first():
            if 'name' in request.data:
                tag.name = request.data['name']
            if 'weight' in request.data:
                tag.weight = request.data['weight']
            tag.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if tag := Tag.objects.filter(pk=id).first():
            tag.delete()
            return Response({'code': 200, 'msg': 'Delete successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
