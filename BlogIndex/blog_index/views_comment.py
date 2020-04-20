from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Article, Comment
from BlogIndex.blog_index.serializer import ManyComment


class CommentView(APIView):
    def get(self, request, id=None):
        article = Article.objects.filter(pk=id).first()
        comments = Comment.objects.filter(article=article)
        data = ManyComment(instance=comments, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})
