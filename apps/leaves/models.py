
# # from django.db import models
# # from django.contrib.auth.models import User

# # class LeaveRequest(models.Model):
# #     LEAVE_TYPE_CHOICES = [
# #         ('sick', 'Sick Leave'),
# #         ('vacation', 'Vacation'),
# #         ('unpaid', 'Unpaid Leave'),
# #     ]

# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
# #     start_date = models.DateField()
# #     end_date = models.DateField()
# #     reason = models.TextField()
# #     status = models.CharField(max_length=20, default='pending')

# #     def __str__(self):
# #         return f"{self.user.username} - {self.leave_type} ({self.status})"









# from django.db import models
# from django.contrib.auth.models import User

# class LeaveRequest(models.Model):
#     LEAVE_TYPE_CHOICES = [
#         ('sick', 'Sick Leave'),
#         ('vacation', 'Vacation'),
#         ('unpaid', 'Unpaid Leave'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     reason = models.TextField()
#     status = models.CharField(max_length=20, default='pending')

#     def __str__(self):
#         return f"{self.user.username} - {self.leave_type} ({self.status})"


from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    LEAVE_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=LEAVE_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.leave_type} ({self.status})"