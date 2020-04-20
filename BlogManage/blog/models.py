from django.db import models


class Tab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    index = models.SmallIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog_tab'
        ordering = ['index']


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    describe = models.TextField()
    image = models.CharField(max_length=254, default='')
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_category'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    weight = models.SmallIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_tag'
        ordering = ['weight']


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=254)
    describe = models.TextField()
    image = models.CharField(max_length=254, default='')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    type = models.SmallIntegerField(default=1)
    link = models.CharField(max_length=254, default='')
    commented = models.BooleanField(default=True)
    top = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    level = models.SmallIntegerField(default=1)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog.Tag', related_name='art_tags')
    tab = models.ForeignKey('blog.Tab', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_article'
        ordering = ['-update']


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_comment'
        ordering = ['-date']
