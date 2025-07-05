# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import LeaveRequest  # Import your model

# admin.site.register(LeaveRequest)  # Register it



# from django.contrib import admin
# from .models import LeaveRequest

# @admin.register(LeaveRequest)
# class LeaveRequestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'leave_type', 'start_date', 'end_date', 'status')
#     list_filter = ('status', 'leave_type', 'start_date', 'end_date')
#     search_fields = ('user__username', 'user__first_name', 'user__last_name', 'leave_type')
#     date_hierarchy = 'start_date'
#     ordering = ('-start_date',)
#     actions = ['approve_leaves', 'reject_leaves']

#     def approve_leaves(self, request, queryset):
#         queryset.update(status='Approved')
#     approve_leaves.short_description = "Approve selected leave requests"

#     def reject_leaves(self, request, queryset):
#         queryset.update(status='Rejected')
#     reject_leaves.short_description = "Reject selected leave requests"

from django.contrib import admin
from .models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'leave_type')
    search_fields = ('user__username',)