from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    describe = models.TextField()
    allowed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_category'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_tag'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=254)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    editor = models.CharField(max_length=100, default='markdown')
    content_md = models.TextField()
    content_html = models.TextField()
    type = models.SmallIntegerField(default=1)
    comment = models.BooleanField(default=True)
    publish = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    public = models.BooleanField(default=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog.Tag', related_name='art_tags')

    class Meta:
        db_table = 'blog_article'


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    content_md = models.TextField()

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_comment'
