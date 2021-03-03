from django.db import models

# Create your models here.

class category(models.Model):
    items = models.CharField(max_length=200)