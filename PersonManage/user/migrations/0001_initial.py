# Generated by Django 3.0.4 on 2020-04-01 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('jurisdiction', '0001_initial'),
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('activated', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=254)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='department.Department')),
                ('jurisdiction', models.ManyToManyField(related_name='u_jurisdictions', to='jurisdiction.Jurisdiction')),
                ('role', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='role.Role')),
            ],
            options={
                'db_table': 'person_user',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.IntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0)),
                ('birthday', models.CharField(default='', max_length=100)),
                ('address', models.CharField(max_length=254)),
                ('postal_code', models.CharField(max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'person_user_info',
            },
        ),
    ]
