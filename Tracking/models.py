from django.db import models


# Company
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    website = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    departments = models.CharField(max_length=255)
    position = models.CharField(max_length=2555)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Staff(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #email = models.EmailField(max_length=255)
    #departments = models.CharField(max_length=255)
    #position = models.CharField(max_length=2555)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

Orignal_Condition_CHOICES = [
        ('new', 'Brand-New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('broken','Broken')
    ]


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    serial_number = models.CharField(max_length=255)
    condition = models.CharField(max_length=10, choices=Orignal_Condition_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


CHECKOUT_CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('broken','Broken')
    ]

RETURN_CONDITION_CHOICES = [
        ('good', 'Good'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
        ('broken','Broken')
    ]
from django.utils import timezone
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    checkout_time = models.DateField()
    #checkin_time = models.DateTimeField(null=True, blank=True)
    checkout_quantity = models.SmallIntegerField(default=1)#the asset quantity given to employee
    chekout_note = models.TextField(max_length=1000,null=True)
    checkout_by_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='assignments_checked_out')
    checkout_condition = models.CharField(max_length=10, choices=CHECKOUT_CONDITION_CHOICES, default='good')
    return_quantity = models.SmallIntegerField(default=0)#the quantity returned by employee
    returned_note = models.TextField(max_length=1000,null=True)
    return_time = models.DateTimeField(null=True, blank=True)
    returned_condition = models.CharField(max_length=10, choices=RETURN_CONDITION_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    returned_by_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, related_name='assignments_returned')#who received the asset
    #updated_at = models.DateTimeField(auto_now=True)
    issuing_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.device} assigned to {self.employee} at {self.checkout_time}"
