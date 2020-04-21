import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.department.models import Department
from PersonManage.user.models import User, UserInfo


class UserView(APIView):
    def post(self, request):
        try:
            user = User(username=request.data['username'],
                        email=request.data.get('email', ''),
                        phone=request.data.get('phone', ''),
                        nickname=request.data.get('nickname', ''))
            m = hashlib.md5()
            m.update(request.data.get('password', '123456').encode('utf-8'))
            user.password = m.hexdigest()
            dept = Department.objects.filter(name='default').first()
            user.department = dept
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
