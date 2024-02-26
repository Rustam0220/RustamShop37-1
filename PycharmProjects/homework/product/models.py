from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='продукт')
    price = models.PositiveIntegerField(verbose_name='price')
    image = models.ImageField(upload_to='media/', verbose_name='image_product')
    description = models.TextField(max_length=300,verbose_name='description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created time')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated time')
    quantity = models.PositiveIntegerField(default=1, verbose_name='quantity')
    weight = models.FloatField(verbose_name='weight')
    is_available = models.BooleanField(verbose_name='is available')
    argticul = models.FloatField(verbose_name='argticul')

    def __str__(self):
        return self.name
