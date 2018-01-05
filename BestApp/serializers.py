from rest_framework import serializers
from .models import *


class OutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Output
        fields = ('name','id','project_id')


class ProjectSerializer(serializers.ModelSerializer):

    outputs = OutputSerializer(many=True)

    class Meta:
        model = Project
        fields = ('code','name','outputs','id')