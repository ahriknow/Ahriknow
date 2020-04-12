from rest_framework.response import Response
from rest_framework.views import APIView
from DatabaseManage.database.models import Database
from DatabaseManage.database.serializer import OneDatabase
import time
import random
import string
import MySQLdb
import pymongo


class DatabaseView(APIView):
    def get(self, request):
        dbs = Database.objects.filter(user=request.u)
        data = OneDatabase(instance=dbs, many=True).data
        return Response({'code': 200, 'msg': 'Query was successful!', 'data': data})

    def post(self, request):
        try:
            conn = Connect()
            t = request.data['type']
            db = conn.id_generator()
            pwd = request.data['password']
            conn.create(t, db, db, pwd)
            database = Database(type=t, dbname=db, username=db, password=pwd, user=request.u)
            database.save()
            return Response({
                'code': 200,
                'msg': 'Opera Successfully!',
                'data': {
                    'opera': 'create',
                    'type': t,
                    'database': db,
                    'username': db,
                    'password': pwd
                }
            })
        except Exception as ex:
            return Response({'code': 500, 'msg': str(ex), 'data': None})

    def put(self, request):
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})

    def delete(self, request, id=None):
        if database := Database.objects.filter(pk=id).first():
            conn = Connect()
            t = database.type
            db = database.dbname
            conn.drop(t, db)
            database.delete()
            return Response({
                'code': 200,
                'msg': 'Opera Successfully!',
                'data': {
                    'opera': 'drop',
                    'type': t,
                    'database': db
                }
            })
        return Response({'code': 400, 'msg': 'Data does not exist!', 'data': None})


class Connect:
    server = 'db.ahriknow.com'
    mysql_password = 'Aa12345.'
    mongo_password = 'Aa12345.'
    mongo = f'mongodb://root:{mongo_password}@{server}:27017/'

    def create(self, t, db, name, password=None):
        if t == 'mongo':
            conn = pymongo.MongoClient(self.mongo)
            info = {
                'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                'database': db,
                'username': name,
                'password': password,
                'user': ''
            }
            conn[db]['version'].insert_one(info)
            result = conn[db].command('createUser', name, pwd=password, roles=["dbAdmin"])
            return True if 'ok' in result else False
        elif t == 'mysql':
            mysql = MySQLdb.connect(host=self.server, user="root", password=self.mysql_password, port=3306,
                                    charset='utf8')
            cursor = mysql.cursor()
            cursor.execute(f'create database `{db}` default charset utf8mb4 collate utf8mb4_unicode_ci')
            cursor.execute(f'create user `{name}`@`%` identified by \'{password}\'')
            cursor.execute(f'grant all on `{db}`.* to `{name}`@`%`')
            mysql.commit()
            cursor.close()
            mysql.close()
            return True

    def drop(self, t, db):
        if t == 'mongo':
            conn = pymongo.MongoClient(self.mongo)
            conn[db].command('dropUser', db)
            conn.drop_database(db)
            return True
        elif t == 'mysql':
            mysql = MySQLdb.connect(host=self.server, user="root", password=self.mysql_password, port=3306,
                                    charset='utf8')
            cursor = mysql.cursor()
            cursor.execute(f'drop database if exists `{db}`')
            mysql.commit()
            cursor.close()
            mysql.close()

    def id_generator(self, size=12, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
