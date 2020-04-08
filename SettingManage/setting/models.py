from django.db import models


class Index(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100, unique=True)
    content = models.TextField(default='')

    class Meta:
        db_table = 'setting_index'
