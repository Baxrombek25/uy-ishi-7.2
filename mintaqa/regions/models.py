from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User=get_user_model()

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField(help_text="Area in square kilometers")
    year_founded = models.IntegerField()
    owner = models.ForeignKey(User,get_user_model(), on_delete=models.CASCADE,null=True,blank=True,related_name='regions')

    def __str__(self):
        return self.name