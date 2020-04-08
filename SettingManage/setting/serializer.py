from rest_framework import serializers
from SettingManage.setting.models import Index


class OneIndex(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'
