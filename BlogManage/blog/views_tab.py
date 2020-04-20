from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Tab
from BlogManage.blog.serializer import ManyTab


class TabView(APIView):
    def get(self, request):
        tab = Tab.objects.all()
        data = ManyTab(instance=tab, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            tab = Tab(name=request.data['name'], index=request.data['index'])
            tab.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if tab := Tab.objects.filter(pk=id).first():
            if 'name' in request.data:
                tab.name = request.data['name']
            if 'index' in request.data:
                tab.index = request.data['index']
            tab.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if tab := Tab.objects.filter(pk=id).first():
            tab.delete()
            return Response({'code': 200, 'msg': 'Delete successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
