from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from redis import StrictRedis

from PersonManage.user.models import User


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path.startswith('/admin/'):
            redis = StrictRedis(host=settings.DATABASES['redis']['HOST'],
                                port=settings.DATABASES['redis']['PORT'],
                                db=0,
                                password=settings.DATABASES['redis']['PASS'])
            if token := request.META.get('HTTP_TOKEN'):
                if id := redis.get(token):
                    redis.expire(token, 3600)
                    request.u = User.objects.filter(pk=id).first()
                else:
                    return JsonResponse({'code': 0})
            else:
                return JsonResponse({'code': 0})
        else:
            pass

    def process_response(self, request, response):
        if response.status_code == 404:
            return JsonResponse({'code': 404, 'msg': '404', 'data': None})
        return response
