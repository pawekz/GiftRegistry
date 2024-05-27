from django.db import models

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    purchased = models.BooleanField(default=False)
