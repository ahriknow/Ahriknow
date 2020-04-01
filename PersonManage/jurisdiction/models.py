from django.db import models


class Jurisdiction(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254, unique=True)
    describe = models.TextField(default='')
    identity = models.CharField(max_length=254, unique=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        db_table = 'person_jurisdiction'
