from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Article, Comment
from BlogManage.blog.serializer import OneComment, ManyComment, PageComment


class CommentView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        if id:
            if request.u.username == 'ahriknow':
                article = Article.objects.filter(pk=id, removed=False).first()
            else:
                article = Article.objects.filter(user=request.u, pk=id, removed=False).first()
            comments = Comment.objects.filter(article=article)
        else:
            f = request.query_params.get('from')
            t = request.query_params.get('to')
            if request.u.username == 'ahriknow':
                articles = Article.objects.filter(removed=False)
            else:
                articles = Article.objects.filter(user=request.u, removed=False)
            if f and t:
                articles = articles.filter(update__range=[f, t], removed=False)
            if title := request.query_params.get('article'):
                articles = articles.filter(title__icontains=title, removed=False)
            comments = Comment.objects.filter(article__in=articles)
        pg = PageComment()
        pgs = pg.paginate_queryset(queryset=comments, request=request, view=self)
        data = ManyComment(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res

    def post(self, request):
        try:
            article = Article.objects.filter(pk=request.data['article']).first()
            com = None
            if c := Comment.objects.filter(pk=request.data['parent']).first():
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
