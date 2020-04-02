from django.db import models


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    describe = models.TextField(default='')
    image = models.URLField(default='')
    public = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notebook_book'


class Catalog(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey('notebook.Book', on_delete=models.CASCADE)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        db_table = 'notebook_catalog'


class Content(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    catalog = models.ForeignKey('notebook.Catalog', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notebook_content'
