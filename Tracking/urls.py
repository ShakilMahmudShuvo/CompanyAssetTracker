from django.urls import path
from .swagger import schema_view
from .views import (
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    AssignmentListCreateView,
    AssignmentRetrieveUpdateDestroyView,
    StaffListCreateView, StaffRetrieveUpdateDestroyView 
)

urlpatterns = [
    # Automated API documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company_list_create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company_retrieve_update_destroy'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee_retrieve_update_destroy'),

    # Device URLs
    path('devices/', DeviceListCreateView.as_view(), name='device_list_create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device_retrieve_update_destroy'),

    # Assignment URLs
    path('device-log/', AssignmentListCreateView.as_view(), name='assignment_list_create'),
    path('device-log/<int:pk>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='assignment_retrieve_update_destroy'),

    path('staff/', StaffListCreateView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyView.as_view(), name='staff-detail'),



]
