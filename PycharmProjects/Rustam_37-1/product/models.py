from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d')
    name = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.IntegerField(default=0)
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.rate}'
