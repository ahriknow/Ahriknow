from rest_framework import serializers
from PersonManage.role.models import Role


class OneRole(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class ManyRole(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
