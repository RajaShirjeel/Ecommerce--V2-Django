from django.db import models

from users.models import User
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Wishlist for {self.user.username}'