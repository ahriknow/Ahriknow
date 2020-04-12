from django.db import models


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)
    auth = models.CharField(max_length=254)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'restapi_project'


class Url(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=254)
    method = models.CharField(max_length=10)
    describe = models.CharField(max_length=254)
    url_id = models.CharField(max_length=254)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    project = models.ForeignKey('restapi.Project', on_delete=models.CASCADE)

    class Meta:
        db_table = 'restapi_url'
        ordering = ['path']
