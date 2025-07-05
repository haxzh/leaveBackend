from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation', 'salary', 'is_active', 'is_manager', 'is_admin', 'is_employee')
    list_filter = ('is_active', 'is_manager', 'is_admin', 'is_employee', 'department')
    search_fields = ('user__username', 'user__email', 'designation')