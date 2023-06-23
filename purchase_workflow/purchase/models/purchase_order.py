from django.db import models
from purchase.models.vendor import Vendor
import random

"""
Notes:

- Field Definitions
    - blank= True/False ('required' argument, if blank=False it means it's required)
    - verbose_name= (is the same as string= in Odoo ORM)
    - unique=True (adds a Constraint to the table to ensure that field is unique)
    - null= (Allows a field to have a null value)

- 'Computed' fields
    - Computed fields here are just functions (not stored)
    - We can override the save() to add a computation to a field

- ForeignKey Fields
    - _id is not needed because it is automatically done
"""

class PurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, verbose_name="Vendor")
    order_name = models.CharField(max_length=60,blank=True)
    order_date = models.DateField(verbose_name="Order Date", blank=False)
    delivery_date = models.DateField(verbose_name="Delivery Date",blank=True)

    def save(self, *args, **kwargs):
        if not self.order_name:
            self.order_name = f"{self.vendor_id.name}-{random.randint(10,99)}{self.id}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_name

    class Meta:
        ordering = ['id']
        verbose_name_plural = "PurchaseOrders"