from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from BlogManage.blog.models import Tab, Article, Comment, Category, Follow, Fabulous, View
from PersonManage.user.models import User


class PageArticle(PageNumberPagination):
    page_size = 10
    max_page_size = 30
    page_size_query_param = 'size'
    page_query_param = 'page'


class OneArticle(serializers.ModelSerializer):
    fabulous = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()

    def get_fabulous(self, row):
        return len(Fabulous().a_fabulous(row.id))

    def get_views(self, row):
        return len(View().a_views(row.id))

    class Meta:
        model = Article
        fields = '__all__'


class ManyArticle(serializers.ModelSerializer):
    fabulous = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_fabulous(self, row):
        return len(Fabulous().a_fabulous(row.id))

    def get_views(self, row):
        return len(View().a_views(row.id))

    def get_comments(self, row):
        return row.comment_set.count()

    def get_user(self, row):
        return {'id': row.user.id, 'avatar': row.user.avatar, 'nickname': row.user.nickname,
                'username': row.user.username}

    class Meta:
        model = Article
        fields = '__all__'


class OneUser(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)
    fans = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    def get_fans(self, row):
        fans = Follow().t_fans(row.id)
        return len(fans)

    def get_articles(self, row):
        return row.article_set.filter(removed=False).count()

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'email', 'phone', 'nickname', 'create_time', 'last_login', 'fans',
                  'articles']


class ManyUser(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, row):
        return row.article_set.filter(removed=False).count()

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'nickname', 'articles']


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


class ManyCategory(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
