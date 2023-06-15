from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name