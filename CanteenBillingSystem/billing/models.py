from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    joined_date=models.DateTimeField(default=timezone.now)
    balance = models.IntegerField(default=0)
    locked = models.BooleanField(default=False)
    reset = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    customer = models.ForeignKey(Customer)
    date = models.DateTimeField(default=timezone.now)
    delivered=models.BooleanField(default=False)
    def __str__(self):
        return str(self.date)

class Product(models.Model):
    name = models.CharField(max_length = 40)
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return self.name

class Item(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,default=None)

class Recharge(models.Model):
    code= models.CharField(max_length=16)
    worth = models.IntegerField()
    used = models.BooleanField(default=False)
