from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.PositiveIntegerField()
    area = models.FloatField(help_text="Area in square kilometers")

    def __str__(self):
        return self.name