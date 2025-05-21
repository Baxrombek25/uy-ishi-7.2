from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth import get_user_model


User = get_user_model()

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField(help_text="Area in square kilometers")
    year_founded = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE , null=True,blank=True)
    established_year = models.PositiveIntegerField(null=True, blank=True)
    founded_date = models.DateField(null=True, blank=True)

    def clean(self):
        today = date.today()
        if self.founded_date and self.founded_date > today:
            raise ValidationError("Kelajakdagi sana kiritib bo'lmaydi.")
        if self.established_year and self.established_year > today.year:
            raise ValidationError("Kelajakdagi yil bo'lishi mumkin emas.")
    
    def str(self):
        return self.name
    
class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='provinces')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='provinces')
    established_year = models.PositiveIntegerField(null=True, blank=True)
    founded_date = models.DateField(null=True, blank=True)

    def clean(self):
        today = date.today()
        if self.founded_date and self.founded_date > today:
            raise ValidationError("Kelajakdagi sana mumkin emas.")
        if self.established_year and self.established_year > today.year:
            raise ValidationError("Kelajakdagi yil kiritib bo'lmaydi.")

    def str(self):
        return self.name