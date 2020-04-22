from rest_framework.response import Response
from rest_framework.views import APIView
from BlogIndex.blog_index.serializer import OneUser, ManyCategory
from BlogManage.blog.models import Category, Follow
from PersonManage.user.models import User


class AuthorView(APIView):
    def get(self, request, id=None):
        if id:
            user = User.objects.filter(pk=id).first()
            categories = Category.objects.filter(user=user)
            u = OneUser(instance=user, many=False).data
            cs = ManyCategory(instance=categories, many=True).data
            fan = Follow().is_fan(request.query_params.get('user'), user.id)
            return Response({'code': 200, 'msg': 'OK', 'data': [u, cs, fan]})
