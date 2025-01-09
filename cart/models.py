from django.db import models

from users.models import User
from products.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.user.email}'
    
    @property
    def calculate_total(self):
        total = 0
        for item in self.cart_items.all():
            total += item.quantity * item.product.price

        return total

    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    class Meta: 
        unique_together = ['product', 'cart']

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in {self.cart.user.email}\'s cart'

