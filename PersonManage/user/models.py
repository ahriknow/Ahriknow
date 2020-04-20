from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    avatar = models.CharField(max_length=254, default='http://ahriknow.oss-cn-beijing.aliyuncs.com/avatar.jpg')
    activated = models.BooleanField(default=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    nickname = models.CharField(max_length=254)
    create_time = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    department = models.ForeignKey('department.Department', null=True, default=None, on_delete=models.SET_DEFAULT)

    roles = models.ManyToManyField('role.Role', related_name='u_roles')
    jurisdictions = models.ManyToManyField('jurisdiction.Jurisdiction', related_name='u_jurisdictions')

    class Meta:
        db_table = 'person_user'
        ordering = ['-create_time']


choice = (
    (0, '保密'),
    (1, '男'),
    (2, '女'),
)


class UserInfo(models.Model):
    name = models.CharField(max_length=254, default='')  # 姓名
    age = models.IntegerField(default=0)  # 年龄
    sex = models.IntegerField(default=0, choices=choice)  # 性别
    birthday = models.CharField(max_length=100, default='')  # 生日
    address = models.CharField(max_length=254)  # 通信地址
    postal_code = models.CharField(max_length=14)  # 邮政编码

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'person_user_info'
