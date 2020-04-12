from rest_framework import serializers
from DatabaseManage.database.models import Database


class OneDatabase(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ['id', 'type', 'dbname', 'username', 'password']
