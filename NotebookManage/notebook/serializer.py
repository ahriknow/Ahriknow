from rest_framework import serializers
from NotebookManage.notebook.models import Book, Catalog, Content


class OneBook(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ManyBook(serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()

    def get_nickname(self, row):
        return row.user.nickname

    class Meta:
        model = Book
        fields = '__all__'
