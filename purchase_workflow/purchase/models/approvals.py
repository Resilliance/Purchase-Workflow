from django.db import models

class Approvals(models.Model):
    APPROVAL_TYPES = [
        ('rfq','Request for Quotation'),
        ('bil','Vendor Bill'),
        ('pos','Purchase Order'),
    ]

    def __str__(self):
        return self.name
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True,null=True,unique=True)
    approval_type = models.CharField(max_length=3,choices=APPROVAL_TYPES)

    