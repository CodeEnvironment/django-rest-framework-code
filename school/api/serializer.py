from rest_framework import serializers
from school.models import Modules, Students


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['id', 'module_name', 'module_duration', 'class_room']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'age', 'grade', 'modules']
        depth = 1
