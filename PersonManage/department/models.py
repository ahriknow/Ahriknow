from django.db import models


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    describe = models.TextField(default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True)

    jurisdictions = models.ManyToManyField('jurisdiction.Jurisdiction', related_name='dept_jurisdictions')

    class Meta:
        db_table = 'person_department'
