# from rest_framework import viewsets
# from .models import LeaveRequest
# from .serializers import LeaveRequestSerializer

# class LeaveRequestViewSet(viewsets.ModelViewSet):
#     queryset = LeaveRequest.objects.all()
#     serializer_class = LeaveRequestSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# from rest_framework import viewsets, permissions
# from .models import LeaveRequest
# from .serializers import LeaveRequestSerializer

# class LeaveRequestViewSet(viewsets.ModelViewSet):
#     queryset = LeaveRequest.objects.all()
#     serializer_class = LeaveRequestSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


from rest_framework import viewsets, permissions
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Admin sees all, user sees only their own
        user = self.request.user
        if user.is_staff:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(user=user)