from rest_framework import viewsets, filters,permissions
from .models import Region
from .serializers import RegionSerializer
from .permissions import IsOwnerOrSuperUser
from django_filters.rest_framework import DjangoFilterBackend

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    filterset_fields = ['country']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrSuperUser()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
