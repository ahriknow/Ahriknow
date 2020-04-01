from rest_framework import serializers
from PersonManage.department.models import Department


class OneDepartment(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class ManyDepartment(serializers.ModelSerializer):
    p_name = serializers.SerializerMethodField()

    def get_p_name(self, row):
        return row.parent.name if row.parent else '顶级部门'

    class Meta:
        model = Department
        fields = ['id', 'name', 'describe', 'create_time', 'update_time', 'parent', 'p_name', 'jurisdictions']
