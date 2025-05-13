from django.db import models
# Create your models here.


class Parking(models.Model):
    Frame_Number = models.IntegerField()
    Spot_Index = models.IntegerField()
    Spot_Status = models.BooleanField()
