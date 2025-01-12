from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    profile_pic = models.ImageField(upload_to='static/profile_pics/', blank=True, null=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email}'
