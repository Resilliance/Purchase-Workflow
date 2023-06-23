from django.db import models

class Vendor(models.Model):
    def __str__(self):
        return self.name
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, unique=True)
    email = models.CharField(max_length=75)

    phone = models.CharField(max_length=15,blank=True,null=True,unique=True,verbose_name="Phone")
    street_1 = models.CharField(max_length=100,blank=True,null=True,verbose_name="Street Address 1")
    street_2 = models.CharField(max_length=100,blank=True,null=True,verbose_name="Street Address 2")
    city = models.CharField(max_length=100,blank=True,null=True,verbose_name="City")
    state = models.CharField(max_length=100,blank=True,null=True,verbose_name="State")
    country = models.ForeignKey('Country',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Vendors"