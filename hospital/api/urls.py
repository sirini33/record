from django.urls import path
from .views import DepartmentList, DepartmentDetail, PatientRecordList, PatientRecordDetail

# from .views import DepartmentListCreateView, PatientRecordListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    # path('patient-records/', PatientRecordListCreateView.as_view(), name='patient-record-list-create'),
    # path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    # path('patient-records/', PatientRecordListCreateView.as_view(), name='patient-record-list-create'),
    path('departments/', DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetail.as_view(), name='department-detail'),
    path('patient_records/', PatientRecordList.as_view(), name='patient-record-list'),
    path('patient_records/<int:pk>/', PatientRecordDetail.as_view(), name='patient-record-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
