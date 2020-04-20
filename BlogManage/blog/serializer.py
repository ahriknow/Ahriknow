from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from BlogManage.blog.models import Tab, Category, Tag, Article, Comment


class PageArticle(PageNumberPagination):
    page_size = 2
    max_page_size = 100
    page_size_query_param = 'size'
    page_query_param = 'page'


class ManyTab(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'


class ManyCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OneTag(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ManyTag(serializers.ModelSerializer):
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
    class Meta:
        model = Article
        fields = '__all__'


class ManyComment(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    def get_article(self, row):
        return row.article.title

    class Meta:
        model = Comment
        fields = '__all__'


class OneComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
