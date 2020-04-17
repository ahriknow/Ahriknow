from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Article, Comment
from BlogManage.blog.serializer import OneComment, ManyComment


class CategoryView(APIView):
    def get(self, request, id=None):
        if id:
            if article := Article.objects.filter(pk=id).first():
                comment = Comment.objects.filter(article=article)
                data = ManyComment(instance=comment, many=True).data
                return Response({'code': 200, 'msg': 'Create successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        comment = Comment.objects.all()
        data = ManyComment(instance=comment, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            article = Article.objects.filter(pk=request.data['article']).first()
            com = None
            if c := Comment.objects.filter(article=article):
                com = c
            comment = Comment(content=request.data['content'], user=request.u,
                              article=article, parent=com)
            comment.save()
            data = OneComment(instance=comment, many=False).data
            return Response({'code': 200, 'msg': 'Create successful!', 'data': data})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def delete(self, request, id=None):
        if comment := Comment.objects.filter(pk=id).first():
            comment.delete()
            return Response({'code': 200, 'msg': 'Delete successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
