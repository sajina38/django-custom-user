from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    release_date = models.DateField(blank = True, nul = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.name # object ko name ko lagi

    