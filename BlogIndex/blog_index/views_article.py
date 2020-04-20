from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Article, Tab
from BlogIndex.blog_index.serializer import OneArticle, ManyArticle, PageArticle


class ArticleView(APIView):
    def get_article_default(self, request):
        articles = Article.objects.filter(removed=False)
        pg = PageArticle()
        pgs = pg.paginate_queryset(queryset=articles, request=request, view=self)
        data = ManyArticle(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res

    def get_article_tab(self, request):
        tab = Tab.objects.filter(pk=request.query_params.get('id')).first()
        articles = Article.objects.filter(removed=False, tab=tab)
        pg = PageArticle()
        pgs = pg.paginate_queryset(queryset=articles, request=request, view=self)
        data = ManyArticle(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res

    def get_article(self, id):
        article = Article.objects.filter(pk=id).first()
        data = OneArticle(instance=article, many=False).data
        return Response({'code': 200, 'msg': 'OK', 'data': data})

    def get(self, request, id=None):
        if id:
            return self.get_article(id)
        if 'id' in request.query_params and int(request.query_params['id']) > 0:
            return self.get_article_tab(request)
        return self.get_article_default(request)
