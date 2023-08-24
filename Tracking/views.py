from rest_framework import generics, status
from rest_framework.response import Response

from .models import Company, Employee, Device, DeviceLog, Staff
from .serializers import CompanySerializer, EmployeeSerializer, DeviceLogSerializer, StaffSerializer, DeviceSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    """ This view handles the GET and POST requests to retrieve a
    list of all companies or create a new company respectively. """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Here add any custom logic before saving the object,
        # such as setting default fields or validating certain fields
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ This view handles GET, PUT, PATCH and DELETE requests to
    retrieve, update or delete a specific company object. """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset


class EmployeeListCreateView(generics.ListCreateAPIView):
    """ This view handles the GET and POST requests to retrieve a
    list of all employees or create a new employee respectively.  """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Here add any custom logic before saving the object,
        # such as setting default fields or validating certain fields
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ This view handles GET, PUT, PATCH and DELETE requests to
    retrieve, update or delete a specific employee object. """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset


class DeviceListCreateView(generics.ListCreateAPIView):
    """ This view handles the GET and POST requests to retrieve a
    list of all devices or create a new device respectively. """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = Device.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Here add any custom logic before saving the object,
        # such as setting default fields or validating certain fields
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ This view handles GET, PUT, PATCH and DELETE requests to
    retrieve, update or delete a specific device object. """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = Device.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset


class AssignmentListCreateView(generics.ListCreateAPIView):
    """ This view handles the GET and POST requests to retrieve a list
    of all device-log or create a new assignment respectively. """
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

    def get_queryset(self):
        queryset = DeviceLog.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Here add any custom logic before saving the object,
        # such as setting default fields or validating certain fields
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AssignmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ This view handles GET, PUT, PATCH and DELETE requests to
    retrieve, update or delete a specific assignment object. """
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

    def get_queryset(self):
        queryset = DeviceLog.objects.all()
        # Ensure each one can see their own data only
        # query_param = self.request.query_params.get(self.request.user.company.id)
        # if query_param:
        #     queryset = queryset.filter(my_field=query_param)
        return queryset




class StaffListCreateView(generics.ListCreateAPIView):
    """ This view handles the GET and POST requests to retrieve a
    list of all staff members or create a new staff member respectively. """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_queryset(self):
        queryset = Staff.objects.all()
        # Add any filtering logic here if needed
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class StaffRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ This view handles GET, PUT, PATCH, and DELETE requests to
    retrieve, update, or delete a specific staff member object. """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_queryset(self):
        queryset = Staff.objects.all()
        # Add any filtering logic here if needed
        return queryset
