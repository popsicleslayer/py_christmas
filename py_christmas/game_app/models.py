from django.db import models

# Create your models here.
class Place(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=200)