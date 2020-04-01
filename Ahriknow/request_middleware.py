from django.utils.deprecation import MiddlewareMixin

from PersonManage.user.models import User


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.u = User.objects.filter(pk=request.META.get('HTTP_TOKEN')).first()

    def process_response(self, request, response):
        return response
