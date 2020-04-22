from rest_framework.response import Response
from rest_framework.views import APIView

from BlogIndex.blog_index.serializer import ManyUser
from BlogManage.blog.models import Follow, Fabulous
from PersonManage.user.models import User


class FabulousView(APIView):
    def post(self, request):
        try:
            f = Fabulous()
            who = request.data.get('who')
            what = request.data.get('what')
            if who and what:
                if 'fabulous' in request.data:
                    if request.data.get('fabulous'):
                        f.fabulous(who, what)
                    else:
                        f.rem(who, what)
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})
