from django.db import models


class Item(models.Model):
    shortDescription = models.CharField(max_length=100)
    price = models.CharField(max_length=10)


class Receipt(models.Model):
    retailer = models.CharField(max_length=100)
    purchaseDate = models.DateField()
    purchaseTime = models.TimeField()
    items = models.ManyToManyField(Item)
    total = models.CharField(max_length=10)



