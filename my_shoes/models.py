from django.db import models

class My_shoes(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_num = models.CharField(max_length=50)
    release_date = models.DateField()
    release_price = models.IntegerField()
    purchase_date = models.DateField()
    purchase_price = models.IntegerField()

    def __str__(self):
        return self.model_name

class Review(models.Model):
    my_shoes = models.ForeignKey(My_shoes, on_delete=models.CASCADE, related_name = 'reviews')
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)