from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Category, Tag, Article, Tab
from BlogManage.blog.serializer import OneArticle, ManyArticle, PageArticle


class ArticleView(APIView):
    def get(self, request, id=None):
        if id:
            if article := Article.objects.filter(pk=id).first():
                data = OneArticle(instance=article, many=False).data
                return Response({'code': 200, 'msg': 'Create successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        if 'category' in request.query_params and int(request.query_params['category']) > 0:
            category = Category.objects.filter(pk=request.query_params['category']).first()
            article = Article.objects.filter(user=request.u, category=category, removed=False)
        else:
            article = Article.objects.filter(user=request.u, removed=False)
        pg = PageArticle()
        pgs = pg.paginate_queryset(queryset=article, request=request, view=self)
        data = ManyArticle(instance=pgs, many=True).data
        res = pg.get_paginated_response(data)
        return res

    def post(self, request):
        try:
            category = Category.objects.filter(pk=request.data['category']).first()
            tab = Tab.objects.filter(pk=request.data['tab']).first()
            article = Article(title=request.data['title'], describe=request.data['describe'],
                              image=request.data['image'], content=request.data['content'],
                              type=request.data['type'], link=request.data['link'],
                              commented=request.data['commented'], top=False,
                              draft=request.data['draft'], level=request.data['level'],
                              user=request.u, category=category, tab=tab)
            tags = Tag.objects.filter(pk__in=request.data['tags'])
            article.save()
            for i in tags:
                article.tags.add(i)
            return Response({'code': 200, 'msg': 'Create successful!', 'data': None})
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request, id=None):
        if article := Article.objects.filter(pk=id).first():
            if 'title' in request.data:
                article.title = request.data['title']
            if 'describe' in request.data:
                article.describe = request.data['describe']
            if 'image' in request.data:
                article.image = request.data['image']
            if 'content' in request.data:
                article.content = request.data['content']
            if 'type' in request.data:
                article.type = request.data['type']
            if 'link' in request.data:
                article.link = request.data['link']
            if 'commented' in request.data:
                article.commented = request.data['commented']
            if 'removed' in request.data:
                article.removed = request.data['removed']
            if 'top' in request.data:
                article.top = request.data['top']
            if 'draft' in request.data:
                article.draft = request.data['draft']
            if 'level' in request.data:
                article.level = request.data['level']
            if 'category' in request.data:
                article.category = Category.objects.filter(pk=request.data['category']).first()
            if 'tab' in request.data:
                article.tab = Tab.objects.filter(pk=request.data['tab']).first()
            if 'tags' in request.data:
                article.tags.clear()
                tags = Tag.objects.filter(pk__in=request.data['tags'])
                for i in tags:
                    article.tags.add(i)
                article.content_html = request.data['tags']
            article.save()
            return Response({'code': 200, 'msg': 'Update successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if article := Article.objects.filter(pk=id).first():
            article.removed = True
            article.save()
            return Response({'code': 200, 'msg': 'Delete successful!', 'data': None})
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
