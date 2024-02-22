from django.db import models

class My_shoes(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_num = models.CharField(max_length=50)
    release_date = models.DateField()
    release_price = models.IntegerField()
    purchase_date = models.DateField()
    purchase_price = models.IntegerField()