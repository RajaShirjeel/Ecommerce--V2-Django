from django.db import models
from django.utils.timezone import now
from django.db.models import Q

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=700, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField('Color', related_name='products')
    sizes = models.ManyToManyField('Size', related_name='products')
    views = models.PositiveIntegerField(default=0)

    @property
    def on_sale(self):
        active_sales = Sale.objects.filter(active = True, start_date__lte=now(), end_date__gte=now()).filter(Q(products=self) | Q(categories=self.category))
        return active_sales.exists()

    def sale_price(self):
        active_sales = Sale.objects.filter(active = True, start_date__lte=now(), end_date__gte=now()).filter(Q(products=self) | Q(categories=self.category))
        if active_sales:
            max_discount = max(sale.discount_percentage for sale in active_sales)
            return self.price - (self.price * max_discount / 100)
        return self.price
            

    @property
    def average_rating(self):
        comments = self.comments.all()
        if not comments.exists():
            return 0
        total = sum(comments.rating for comments in comments)
        return total / comments.count()

    
    def __str__(self):
        return f'{self.name}-{self.price}'
    

class Category(models.Model):
    type = models.CharField(max_length=100, blank=False, null=False)

    @property
    def on_sale(self):
        active_sales = Sale.objects.filter(active = True, start_date__lte=now(), end_date__gte=now()).filter(categories=self)
        return active_sales.exists()

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
    image = models.ImageField(upload_to='static/product_images/', blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')

    def __str__(self):
        return f'Image for ${self.product.name}'
    

class Sale(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    discount_percentage = models.IntegerField(blank=False, null=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField('Product', related_name='sales')
    categories = models.ManyToManyField('Category', related_name='sales')

    def save(self, *args, **kwargs):
        current_time = now()
        if self.start_date <= current_time and current_time <= self.end_date:
            self.active = True
        else:
            self.active = False
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Sale {self.name} - ${self.discount_percentage} % off'