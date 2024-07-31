from rest_framework import serializers
from .models import PatientRecord, Department,Doctor
from django.contrib.auth.models import Group, User
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'department']

    def create(self, validated_data):
        department_data = validated_data.pop('department')
        department, _ = Department.objects.get_or_create(**department_data)
        user = User.objects.create(**validated_data['user'])
        return Doctor.objects.create(user=user, department=department)

    def update(self, instance, validated_data):
        department_data = validated_data.pop('department')
        instance.user.username = validated_data['user'].get('username', instance.user.username)
        instance.user.save()

        department, _ = Department.objects.get_or_create(**department_data)
        instance.department = department
        instance.save()
        return instance