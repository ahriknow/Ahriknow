from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from NotebookManage.notebook.models import Book, Catalog, Content


class PageBook(PageNumberPagination):
    page_size = 10


class ManyBook(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()

    def get_nickname(self, row):
        return row.user.nickname

    class Meta:
        model = Book
        fields = '__all__'


class ManyCatalog(serializers.ModelSerializer):
    p_name = serializers.SerializerMethodField()

    def get_p_name(self, row):
        return row.parent.name if row.parent else '顶级目录'

    class Meta:
        model = Catalog
        fields = '__all__'


class OneContent(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
