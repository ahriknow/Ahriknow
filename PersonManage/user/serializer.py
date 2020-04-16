from rest_framework import serializers
from PersonManage.user.models import User, UserInfo


class OneUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ManyUser(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()

    def get_userinfo(self, row):
        ui = UserInfo.objects.filter(user=row).first()
        return OneUserinfo(instance=ui, many=False).data

    def get_password(self, row):
        return ''

    class Meta:
        model = User
        fields = '__all__'


class LoginInfo(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField()

    def get_userinfo(self, row):
        ui = UserInfo.objects.filter(user=row).first()
        return OneUserinfo(instance=ui, many=False).data

    class Meta:
        model = User
        fields = '__all__'


class OneUserinfo(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
