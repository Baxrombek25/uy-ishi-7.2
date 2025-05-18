from django.db import models
from accounts.models import CustomUser

class Region(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='regions')

    def str(self):
        return self.name