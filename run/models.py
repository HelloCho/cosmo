from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ProductModel(models.Model):
    code = models.CharField(max_length = 2, null=False)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return "%s" % (self.name)

class Product(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(default = 0, null=False)
    madeYear = models.CharField(max_length=4, choices=[(str(year), str(year)) for year in range(datetime.datetime.now().year, 2013, -1)], default=datetime.datetime.now().year)
    isDisposal = models.BooleanField(default = False)

    def __str__(self):
        return "%s - %s" % (self.product.name, self.madeYear)
