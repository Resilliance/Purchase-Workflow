from django.db import models

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True) 
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"