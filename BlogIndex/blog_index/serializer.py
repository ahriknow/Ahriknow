from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from BlogManage.blog.models import Tab, Article, Comment


class PageArticle(PageNumberPagination):
    page_size = 10
    max_page_size = 30
    page_size_query_param = 'size'
    page_query_param = 'page'


class OneArticle(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ManyArticle(serializers.ModelSerializer):
    fabulous = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_fabulous(self, row):
        return 154

    def get_views(self, row):
        return 263

    def get_user(self, row):
        return {'avatar': row.user.avatar, 'nickname': row.user.nickname}

    class Meta:
        model = Article
        fields = '__all__'


class ManyTab(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'


class ManyComment(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, row):
        return {'avatar': row.user.avatar, 'nickname': row.user.nickname}

    class Meta:
        model = Comment
        fields = '__all__'
