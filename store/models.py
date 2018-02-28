from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
# Create your models here.

# Item related entities

class items(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class tag(models.Model):
    tagName = models.CharField(max_length=15)

class hadTag(models.Model):
    itemName = models.ForeignKey(items, on_delete=models.CASCADE)
    itemTag = models.ForeignKey(tag, on_delete=models.CASCADE)

class person(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

    #validate_phone = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(max_length=17)

class seller(models.Model):
    companyName = models.CharField(max_length=35)
    owner = models.ForeignKey(person, on_delete=models.CASCADE)

class sells(models.Model):
    seller = models.ForeignKey(seller, on_delete=models.CASCADE)
    item = models.ForeignKey(items, on_delete=models.CASCADE,
                             blank=True)  # validators should be a list

class users(models.Model):
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    Email = models.EmailField()
    userName = models.CharField(max_length = 15).unique
    password = models.CharField(max_length= 128)

    premium = models.BooleanField()
    created = models.DateField(default=datetime.now, blank=True)
