from rest_framework import serializers
from PersonManage.jurisdiction.models import Jurisdiction


class OneJurisdiction(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = "__all__"


class ManyJurisdiction(serializers.ModelSerializer):
    p_name = serializers.SerializerMethodField()

    def get_p_name(self, row):
        return row.parent.name if row.parent else '顶级权限'

    class Meta:
        model = Jurisdiction
        fields = "__all__"


class ManyJurisdictionId(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = ['identity']
