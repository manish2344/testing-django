# globalapp/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
