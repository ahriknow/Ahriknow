from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from BlogManage.blog.models import Tab, Category, Tag, Article, Comment


class PageArticle(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'size'
    page_query_param = 'page'


class PageComment(PageNumberPagination):
    page_size = 20
    max_page_size = 100
    page_size_query_param = 'size'
    page_query_param = 'page'


class ManyTab(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Tab
        fields = '__all__'


class ManyCategory(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class OneTag(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class ManyTag(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
        depth = 2


class OneArticle(serializers.ModelSerializer):
    select = serializers.SerializerMethodField()

    def get_select(self, row):
        return ManyTag(instance=row.tags, many=True).data

    class Meta:
        model = Article
        fields = '__all__'


class ManyArticle(serializers.ModelSerializer):
    update = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ManyComment(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    def get_article(self, row):
        return row.article.title

    class Meta:
        model = Comment
        fields = '__all__'


class OneComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
