from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    is_mvp = models.BooleanField(default=False)
    def __str__(self):
        return self.name