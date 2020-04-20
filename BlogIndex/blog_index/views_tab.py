from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Tab
from BlogIndex.blog_index.serializer import ManyTab


class TabView(APIView):
    def get(self, request):
        tab = Tab.objects.all()
        data = ManyTab(instance=tab, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
