from django.db import models

# Create your models here.
class Productmodel(models.Model):
    id = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    dateofdelivery = models.CharField(max_length=255)
    dateofshipping = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amountpaid = models.CharField(max_length=255)
    pendingamount= models.CharField(max_length=255)
    date= models.CharField(max_length=255)
    shippingmode= models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Calendarmodel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    

    def __str__(self):
        return self.date