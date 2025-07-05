



from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LeaveRequestViewSet

router = DefaultRouter()
router.register(r'leaverequest', LeaveRequestViewSet)

urlpatterns = router.urls
