from rest_framework import viewsets, filters
from .models import Region
from .serializers import RegionSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    filterset_fields = ['country']