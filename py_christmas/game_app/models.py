from django.db import models

# Create your models here.
class Place(models.Model):
    description = models.TextField()
    short_description = models.CharField(max_length=200)

class Way(models.Model):
    source = models.ForeignKey(Place, related_name='outgoing_ways', on_delete=models.CASCADE)
    destination = models.ForeignKey(Place, related_name='incoming_ways', on_delete=models.CASCADE)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    gain = models.IntegerField(default=0)