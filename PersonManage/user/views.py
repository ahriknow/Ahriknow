import hashlib
from django.conf import settings
from redis import StrictRedis
from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.department.models import Department
from PersonManage.jurisdiction.models import Jurisdiction
from PersonManage.role.models import Role
from PersonManage.user.models import User, UserInfo
from PersonManage.user.serializer import OneUser, ManyUser


class UserView(APIView):
    def get(self, request, id=None):
        if id:
            if user := User.objects.filter(pk=id).first():
                data = OneUser(instance=user, many=False).data
                return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        else:
            users = User.objects.all()
            data = ManyUser(instance=users, many=True).data
            return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            user = User(username=request.data['username'],
                        email=request.data.get('email', ''),
                        phone=request.data.get('phone', ''),
                        nickname=request.data.get('nickname', ''))
            m = hashlib.md5()
            m.update(request.data.get('password', '123456').encode('utf-8'))
            user.password = m.hexdigest()
            if department := request.data.get('department'):
                dept = Department.objects.filter(pk=department).first()
                if dept:
                    user.department = dept
            if role := request.data.get('role'):
                r = Role.objects.filter(pk=role).first()
                if r:
                    user.role = r
            user.save()
            userinfo = UserInfo(user=user)
            if u := request.data.get('userinfo'):
                if name := u.get('name'):
                    userinfo.name = name
                if age := u.get('age'):
                    userinfo.age = age
                if sex := u.get('sex'):
                    userinfo.sex = sex
                if birthday := u.get('birthday'):
                    userinfo.birthday = birthday
            userinfo.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            if 'UNIQUE' in str(ex):
                return Response({'code': 400, 'msg': 'Data duplication!', 'data': None})
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if user := User.objects.filter(pk=id).first():
            data = request.data
            if department := data.get('department'):
                dept = Department.objects.filter(pk=department).first()
                if dept:
                    user.department = dept
                else:
                    return Response({'code': 400, 'msg': "The 'department' does not exist!", 'data': None})
            if role := data.get('role'):
                r = Role.objects.filter(pk=role).first()
                if r:
                    user.role = r
                else:
                    return Response({'code': 400, 'msg': "The 'role' does not exist!", 'data': None})
            if (activated := data.get('activated', '')) in [True, False]:
                user.activated = activated
            if username := data.get('username'):
                user.username = username
            if password := data.get('password'):
                user.password = password
            if email := data.get('email'):
                user.email = email
            if phone := data.get('phone'):
                user.phone = phone
            if nickname := data.get('nickname'):
                user.nickname = nickname
            if 'jurisdiction' in data:
                redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                    port=settings.DATABASES['redis']['PORT'],
                                    db=settings.DATABASES['redis']['NAME_2'],
                                    password=settings.DATABASES['redis']['PASS'])
                redis.flushdb()
                user.jurisdiction.clear()
                if jurisdiction := data['jurisdiction']:
                    jurs = Jurisdiction.objects.filter(pk__in=jurisdiction)
                    for i in jurs:
                        user.jurisdiction.add(i)
            if u := request.data.get('userinfo'):
                userinfo = UserInfo.objects.filter(user=user).first()
                if name := u.get('name'):
                    userinfo.name = name
                if age := u.get('age'):
                    userinfo.age = age
                if sex := u.get('sex'):
                    userinfo.sex = sex
                if birthday := u.get('birthday'):
                    userinfo.birthday = birthday
                userinfo.save()
            user.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if user := User.objects.filter(pk=id).first():
            user.delete()
            return Response({'code': 200, 'msg': 'Delete successful!'})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
