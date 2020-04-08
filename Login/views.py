import hashlib
import time
from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from PersonManage.user.models import User
from PersonManage.user.serializer import OneUser
from redis import StrictRedis


class AuthView(APIView):
    def post(self, request):
        try:
            mp = hashlib.md5()
            mp.update(request.data.get('password', '').encode('utf-8'))
            user = User.objects.filter(
                username=request.data.get('username'),
                password=mp.hexdigest()
            ).first()
            if user:
                if not user.activated:
                    return Response({'code': 401, 'msg': 'This account is not allowed to log in!', 'data': None})
                user.last_login = timezone.now()
                user.save()

                redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                    port=settings.DATABASES['redis']['PORT'],
                                    db=settings.DATABASES['redis']['NAME_1'],
                                    password=settings.DATABASES['redis']['PASS'])
                m = hashlib.md5()
                m.update((user.username + str(time.time())).encode('utf-8'))
                token = m.hexdigest()
                redis.set(token, user.id)
                redis.expire(token, 3600)

                data = OneUser(instance=user, many=False).data
                data.update({'token': token})
                return Response({'code': 200, 'msg': 'Login successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Wrong username or password!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})