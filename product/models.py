from django.db import models

# Create your models here.

class Size(models.Model):
    size_name = models.CharField(max_length=5)

    def __str__(self):
        return self.size_name


class Color(models.Model):
    color_hex = models.CharField(max_length=10)

    def __str__(self):
        return self.color_hex

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=400, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=1, null=False)
    description = models.CharField(max_length=200, null=True)
    quantity = models.PositiveIntegerField(default=0, null=False)
    sizes = models.ManyToManyField(Size, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product_img = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'product image for {self.product.name}'



