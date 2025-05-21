from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='regions')

    def __str__(self):
        return self.name