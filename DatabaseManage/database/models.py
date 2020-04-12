from django.db import models


class Database(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    dbname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'database_db'
        ordering = ['type']
