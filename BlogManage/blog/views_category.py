from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Category
from BlogManage.blog.serializer import ManyCategory


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.filter(user=request.u)
        data = ManyCategory(instance=category, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            category = Category(name=request.data['name'], describe=request.data['describe'],
                                image=request.data['image'], user=request.u)
            category.save()
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if category := Category.objects.filter(pk=id).first():
            if 'name' in request.data:
                category.name = request.data['name']
            if 'describe' in request.data:
                category.describe = request.data['describe']
            if 'image' in request.data:
                category.image = request.data['image']
            if 'allowed' in request.data:
                category.allowed = request.data['allowed']
            category.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if category := Category.objects.filter(pk=id).first():
            category.delete()
            return Response({'code': 200, 'msg': 'Delete successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
