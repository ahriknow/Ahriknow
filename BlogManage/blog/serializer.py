from rest_framework import serializers
from BlogManage.blog.models import Category, Tag, Article, Comment


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
    class Meta:
        model = Article
        fields = '__all__'


class ManyArticle(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ManyComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 5


class OneComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
