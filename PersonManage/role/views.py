from django.conf import settings
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.role.models import Role
from PersonManage.role.serializer import OneRole, ManyRole
from PersonManage.jurisdiction.models import Jurisdiction


class RoleView(APIView):
    def get(self, request, id=None):
        if id:
            if role := Role.objects.filter(pk=id).first():
                data = OneRole(instance=role, many=False).data
                return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        else:
            roles = Role.objects.all()
            data = ManyRole(instance=roles, many=True).data
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            role = Role(name=request.data['name'], describe=request.data['describe'])
            role.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            if 'UNIQUE' in str(ex):
                return Response({'code': 400, 'msg': 'Data duplication!', 'data': None})
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if role := Role.objects.filter(pk=id).first():
            data = request.data
            if name := data.get('name'):
                role.name = name
            if describe := data.get('describe'):
                role.describe = describe
            if 'jurisdictions' in data:
                redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                    port=settings.DATABASES['redis']['PORT'],
                                    db=settings.DATABASES['redis']['NAME_2'],
                                    password=settings.DATABASES['redis']['PASS'])
                redis.flushdb()
                role.jurisdictions.clear()
                for i in data['jurisdictions']:
                    jur = Jurisdiction.objects.filter(pk=i).first()
                    role.jurisdictions.add(jur)
            role.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if role := Role.objects.filter(pk=id).first():
            role.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
