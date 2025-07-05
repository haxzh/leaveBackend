# from rest_framework import serializers
# from .models import LeaveRequest

# class LeaveRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeaveRequest
#         fields = '__all__'



# from rest_framework import serializers
# from .models import LeaveRequest

# class LeaveRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LeaveRequest
#         fields = '__all__'
#         read_only_fields = ['user', 'status']



from rest_framework import serializers
from .models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = LeaveRequest
        fields = '__all__'