from django.conf import settings
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.jurisdiction.models import Jurisdiction
from PersonManage.jurisdiction.serializer import OneJurisdiction, ManyJurisdiction


class JurisdictionView(APIView):
    def get(self, request, id=None):
        if id:
            if jur := Jurisdiction.objects.filter(pk=id).first():
                data = OneJurisdiction(instance=jur, many=False).data
                return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        else:
            jurs = Jurisdiction.objects.all()
            data = ManyJurisdiction(instance=jurs, many=True).data
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            jur = Jurisdiction(name=request.data['name'], describe=request.data['describe'],
                               identity=request.data['identity'])
            if request.data.get('parent'):
                if parent := Jurisdiction.objects.filter(pk=request.data['parent']).first():
                    jur.parent = parent
                else:
                    return Response({'code': 400, 'msg': "The 'parent' does not exist!", 'data': None})
            jur.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            if 'UNIQUE' in str(ex):
                return Response({'code': 400, 'msg': 'Data duplication!', 'data': None})
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if jur := Jurisdiction.objects.filter(pk=id).first():
            data = request.data
            if name := data.get('name'):
                jur.name = name
            if describe := data.get('describe'):
                jur.describe = describe
            if identity := data.get('identity'):
                jur.identity = identity
            jur.save()
            redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                port=settings.DATABASES['redis']['PORT'],
                                db=settings.DATABASES['redis']['NAME_2'],
                                password=settings.DATABASES['redis']['PASS'])
            redis.flushdb()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if jur := Jurisdiction.objects.filter(pk=id).first():
            jur.delete()
            redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                port=settings.DATABASES['redis']['PORT'],
                                db=settings.DATABASES['redis']['NAME_2'],
                                password=settings.DATABASES['redis']['PASS'])
            redis.flushdb()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
