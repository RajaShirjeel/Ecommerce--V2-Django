from django.db import models

from users.models import User
from cart.models import Cart
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def increase_product_order_count(self):
        products = self.cart.cart_items.all()
        
        for product in products:
            product.total_orders += 1
            product.save()

    def __save__(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.increase_product_order_count()

    def __str__(self):
        return f'{self.user}\'s order on {self.created_at}'
