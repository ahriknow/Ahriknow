from rest_framework.response import Response
from rest_framework.views import APIView
from BlogManage.blog.models import Category, Tag, Article
from BlogManage.blog.serializer import OneArticle, ManyArticle


class CategoryView(APIView):
    def get(self, request, id=None):
        if id:
            if article := Article.objects.filter(pk=id).first():
                data = OneArticle(instance=article, many=False).data
                return Response({'code': 200, 'msg': 'Create successful!', 'data': data})
            return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})
        article = Article.objects.filter(user=request.u)
        data = ManyArticle(instance=article, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            category = Category.objects.filter(pk=id).first()
            article = Article(title=request.data['title'], describe=request.data['describe'],
                              image=request.data['image'], editor=request.data['editor'],
                              content_md=request.data['content_md'], content_html=request.data['content_html'],
                              type=request.data['type'], commented=request.data['commented'],
                              published=request.data['published'], removed=request.data['removed'],
                              draft=request.data['draft'], level=request.data['level'],
                              user=request.u, category=category)
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
            if 'editor' in request.data:
                article.editor = request.data['editor']
            if 'content_md' in request.data:
                article.content_md = request.data['content_md']
            if 'content_html' in request.data:
                article.content_html = request.data['content_html']
            if 'type' in request.data:
                article.type = request.data['type']
            if 'commented' in request.data:
                article.commented = request.data['commented']
            if 'published' in request.data:
                article.published = request.data['published']
            if 'removed' in request.data:
                article.removed = request.data['removed']
            if 'draft' in request.data:
                article.draft = request.data['draft']
            if 'level' in request.data:
                article.level = request.data['level']
            if 'category' in request.data:
                article.category = Category.objects.filter(pk=request.data['category']).first()
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
