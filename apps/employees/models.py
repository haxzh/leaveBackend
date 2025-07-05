from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_joining = models.DateField()
    leave_balance = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
     verbose_name_plural = 'Employees'
     ordering = ['-created_at']
     permissions = [
        ('view_department', 'Can view department'),
        ('change_department', 'Can change department'),
        ('delete_department', 'Can delete department'),
        ('add_department', 'Can add department'),
        ('view_designation', 'Can view designation'),
        ('change_designation', 'Can change designation'),
        ('delete_designation', 'Can delete designation'),
        ('add_designation', 'Can add designation'),
    ]