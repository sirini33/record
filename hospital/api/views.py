# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from .models import PatientRecord, Department
# from .serializers import PatientRecordSerializer, DepartmentSerializer

# class DepartmentListCreateView(generics.ListCreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#     permission_classes = [permissions.AllowAny]

# class PatientRecordListCreateView(generics.ListCreateAPIView):
#     queryset = PatientRecord.objects.all()
#     serializer_class = PatientRecordSerializer
#     permission_classes = [permissions.AllowAny]
#     # def perform_create(self, serializer):
#     #     serializer.save(patient=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientRecord, Department
from .serializers import PatientRecordSerializer, DepartmentSerializer

class DepartmentList(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    def get_department_by_pk(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return None

    def get(self, request, pk):
        department = self.get_department_by_pk(pk)
        if department is not None:
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        return Response({'error': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        department = self.get_department_by_pk(pk)
        if department is not None:
            serializer = DepartmentSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        department = self.get_department_by_pk(pk)
        if department is not None:
            serializer = DepartmentSerializer(department, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        department = self.get_department_by_pk(pk)
        if department is not None:
            department.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND)


class PatientRecordList(APIView):
    def get(self, request):
        patient_records = PatientRecord.objects.all()
        serializer = PatientRecordSerializer(patient_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientRecordDetail(APIView):
    def get_patient_record_by_pk(self, pk):
        try:
            return PatientRecord.objects.get(pk=pk)
        except PatientRecord.DoesNotExist:
            return None

    def get(self, request, pk):
        patient_record = self.get_patient_record_by_pk(pk)
        if patient_record is not None:
            serializer = PatientRecordSerializer(patient_record)
            return Response(serializer.data)
        return Response({'error': 'Patient record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        patient_record = self.get_patient_record_by_pk(pk)
        if patient_record is not None:
            serializer = PatientRecordSerializer(patient_record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Patient record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        patient_record = self.get_patient_record_by_pk(pk)
        if patient_record is not None:
            serializer = PatientRecordSerializer(patient_record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Patient record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        patient_record = self.get_patient_record_by_pk(pk)
        if patient_record is not None:
            patient_record.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Patient record does not exist'}, status=status.HTTP_404_NOT_FOUND)
