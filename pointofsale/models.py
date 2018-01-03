from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.full_clean()
        super(Product, self).save(*args, **kwargs)



