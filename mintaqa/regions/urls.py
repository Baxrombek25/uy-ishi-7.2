from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, ProvinceViewSet

router = DefaultRouter()
router.register('regions', RegionViewSet, basename='region')
router.register('provinces', ProvinceViewSet, basename='province')

urlpatterns = [
    path('', include(router.urls)),
]