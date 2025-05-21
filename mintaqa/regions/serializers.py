from rest_framework import serializers
from .models import Region
from datetime import date
from .models import Province

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        read_only_fields=['owner']

    def validate_year_founded(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Kelajakdagi yillar kiritilishi mumkin emas.")
        return value

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        read_only_fields = ['owner']