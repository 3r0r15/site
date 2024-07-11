from django.db import models

# Create your models here.
class Product ( models.Model) :
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    price = models.IntegerField()
    image_Url = models.CharField(max_length=256)

    range = models.CharField(max_length=128,null=True, blank=True)
    def __str__(self):
        return f'{self.name}'