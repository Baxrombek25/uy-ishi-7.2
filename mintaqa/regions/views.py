from rest_framework import viewsets, filters,permissions
from .models import Region
from .models import Province
from .serializers import ProvinceSerializer
from .serializers import RegionSerializer
from .permissions import IsOwnerOrSuperUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    filterset_fields = ['country']
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwnerOrSuperUser()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def perform_update(self, serializer):
        region = self.get_object()
        if not (self.request.user == region.owner or self.request.user.is_superuser):
            raise PermissionDenied("Faqat owner yoki admin o‘zgartira oladi.")
        serializer.save()

    def perform_destroy(self, instance):
        if not (self.request.user == instance.owner or self.request.user.is_superuser):
            raise PermissionDenied("Faqat owner yoki admin o‘chira oladi.")
        instance.delete()
    
class IsOwnerOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.owner == request.user



class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwnerOrSuperUser()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        province = self.get_object()
        if not (self.request.user == province.owner or self.request.user.is_superuser):
            raise PermissionDenied("Faqat owner yoki superuser o‘zgartira oladi.")
        serializer.save()

    def perform_destroy(self, instance):
        if not (self.request.user == instance.owner or self.request.user.is_superuser):
            raise PermissionDenied("Faqat owner yoki superuser o‘chira oladi.")
        instance.delete()