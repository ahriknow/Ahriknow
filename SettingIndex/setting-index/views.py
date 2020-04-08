from rest_framework.response import Response
from rest_framework.views import APIView
from SettingManage.setting.models import Index
from SettingManage.setting.serializer import OneIndex


class IndexShowView(APIView):
    def get(self, request):
        if index := Index.objects.filter(type='index-show').first():
            data = OneIndex(instance=index, many=False).data
        else:
            index = Index(type='index-show')
            index.save()
            data = OneIndex(instance=index, many=False).data
        return Response({'code': 200, 'msg': 'Update successful!', 'data': data})

    def put(self, request):
        if index := Index.objects.filter(type='index-show').first():
            index.content = request.data.get('content')
            index.save()
        else:
            index = Index(type='index', content=request.data.get('content'))
            index.save()
        return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
