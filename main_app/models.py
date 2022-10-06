from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True)
    img = models.CharField(max_length=500)
    trim = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.make

    class Meta:
        ordering = ['make']


class Engine(models.Model):
    designation = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    induction = models.CharField(max_length = 100)
    configuration = models.CharField(max_length=100)
    horsepower = models.CharField(max_length=100)
    torque = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="engine")

    def __str__(self):
        return self.car


class Tire(models.Model):
    brand = models.CharField(max_length=150)
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.brand



