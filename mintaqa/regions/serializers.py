from rest_framework import serializers
from .models import Region
from datetime import date

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

    def validate_year_founded(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Kelajakdagi yillar kiritilishi mumkin emas.")
        return value
