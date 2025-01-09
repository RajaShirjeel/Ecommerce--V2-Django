from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=700, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField('Color', related_name='products')
    sizes = models.ManyToManyField('Size', related_name='products')

    
    def __str__(self):
        return f'{self.name}-{self.price}'
    

class Category(models.Model):
    type = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f'{self.type}'


class Color(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    hex_code = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.name} - {self.hex_code}'
    

class Size(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')

    def __str__(self):
        return f'Image for ${self.product.name}'
    
