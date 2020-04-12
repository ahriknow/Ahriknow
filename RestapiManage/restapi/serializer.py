from rest_framework import serializers
from RestapiManage.restapi.models import Project, Url


class ManyProject(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ManyUrl(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
