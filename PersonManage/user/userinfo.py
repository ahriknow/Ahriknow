from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.user.models import User, UserInfo
from PersonManage.user.serializer import LoginInfo


class UserinfoView(APIView):
    def get(self, request):
        user = User.objects.filter(pk=request.u.id).first()
        if user:
            data = LoginInfo(instance=user, many=False).data
            return Response({'code': 200, 'msg': 'Get userinfo successfully!', 'data': data})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def put(self, request):
        try:
            if user := User.objects.filter(pk=request.u.id).first():
                if 'phone' in request.data or 'email' in request.data:
                    if email := request.data.get('email'):
                        user.email = email
                    if phone := request.data.get('phone'):
                        user.phone = phone
                    if nickname := request.data.get('nickname'):
                        user.nickname = nickname
                    user.save()
                else:
                    if userinfo := UserInfo.objects.filter(user=user).first():
                        if name := request.data.get('name'):
                            userinfo.name = name
                        if age := request.data.get('age'):
                            userinfo.age = age
                        if sex := request.data.get('sex'):
                            userinfo.sex = sex
                        if birthday := request.data.get('birthday'):
                            userinfo.birthday = birthday
                        userinfo.save()
                    else:
                        return Response({'code': 400, 'msg': "The 'userinfo' does not exist!", 'data': None})
                return Response({'code': 200, 'msg': 'Update userinfo successful!', 'data': None})
            return Response({'code': 400, 'msg': "The 'user' does not exist!", 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})
