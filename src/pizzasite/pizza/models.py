from django.db import models

# Create your models here.
class Deal(models.Model):
    modifier = models.FloatField()
    deal_name = models.CharField(max_length=200)

    def __str__(self):
        return self.deal_name

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    # deal = models.ForeignKey(Deal, on_delete=models.CASCADE, required=False)

    def __str__(self):
        return self.pizza_name
