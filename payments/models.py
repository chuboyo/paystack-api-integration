
from django.db import models

currencyy = [
    ('ngn', 'NGN'),
    ('usd', 'USD')
]

# Create your models here.

class Payments(models.Model):
    amount = models.IntegerField()
    currencyy = models.CharField(max_length=3, choices=currencyy, default='ngn')
    email = models.CharField(max_length=50)
    ref = models.IntegerField()


    def __str__(self):
        return str(self.amount)

   
