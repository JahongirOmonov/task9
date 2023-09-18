from django.db import models
from django.contrib.auth.models import User

class notebooks(models.Model):
    name = models.CharField(max_length=212, default='')
    count = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name


class Bolalar(models.Model):
    name = models.CharField(max_length=181, default='')
    number = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name