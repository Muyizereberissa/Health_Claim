from rest_framework.routers import DefaultRouter
from .views import ClaimViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'claims', ClaimViewSet, basename='claim')

# Use router.urls for urlpatterns
urlpatterns = router.urls