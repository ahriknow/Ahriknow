from rest_framework.response import Response
from rest_framework.views import APIView

from BlogIndex.blog_index.serializer import ManyUser
from BlogManage.blog.models import Follow
from PersonManage.user.models import User


class FollowView(APIView):
    def get(self, request):
        f = Follow()
        ids = list(f.my_follow(request.query_params.get('id')))
        users = User.objects.filter(pk__in=ids)
        data = ManyUser(instance=users, many=True).data
        return Response({'code': 200, 'msg': 'Create successful!', 'data': data})

    def post(self, request):
        try:
            f = Follow()
            who = request.data.get('who')
            what = request.data.get('what')
            if who and what:
                if 'fans' in request.data:
                    if request.data.get('fans'):
                        f.follow(who, what)
                    else:
                        f.rem(who, what)
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})
