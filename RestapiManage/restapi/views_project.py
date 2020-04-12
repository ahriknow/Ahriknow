import hashlib
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from RestapiManage.restapi.models import Project
from RestapiManage.restapi.serializer import ManyProject


class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.filter(user=request.u)
        data = ManyProject(instance=projects, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            auth = m.hexdigest()
            data = request.data
            project = Project(name=data.get('name'), describe=data.get('describe'), auth=auth, user=request.u)
            project.save()
            return Response({'code': 200, 'msg': 'Opera Successfully!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request):
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if project := Project.objects.filter(pk=id).first():
            project.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
