from django.db import models
# from .vendor import Vendor

class Product(models.Model):
    PRODUCT_TYPES = [
        ('stor','Storable'),
        ('cons','Consumable'),
        ('serv','Service'),
    ]

    def __str__(self):
        return self.name
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(verbose_name="Description", null=True)
    prod_type = models.CharField(max_length=4,choices=PRODUCT_TYPES, blank=False,default="stor")

    quantity = models.IntegerField(verbose_name="Quantity", null=True, default=0)
    reserved_quantity = models.IntegerField(verbose_name="Reserved Quantity", null=True, default=0)
    available_quantity = models.IntegerField(verbose_name="Available Quantity", null=True, default=0)

    length = models.FloatField(verbose_name="Length", null=True)
    width = models.FloatField(verbose_name="Width", null=True)
    height = models.FloatField(verbose_name="Height", null=True)
    weight = models.FloatField(verbose_name="Weight", null=True)
    volume = models.FloatField(verbose_name="Volume", null=True)

    supplier_ids = models.ManyToManyField('Vendor')



