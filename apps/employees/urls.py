# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EmployeeViewSet

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]


from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserInfoView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', UserInfoView.as_view(), name='user-info'),
]
