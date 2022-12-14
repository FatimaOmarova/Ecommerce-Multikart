from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser, User



class User(AbstractUser):
    phone_number = models.CharField(
        max_length=128,
    )
    message = models.TextField()
    flat = models.CharField(
        max_length=128,
    )
    address = models.TextField()
    country = models.CharField(
        max_length=128,
    )
    city = models.CharField(
        max_length=128,
    )
    state = models.CharField(
        max_length=128,
    )
    zip_code = models.IntegerField(null=True, blank=True) 
    
    def __str__(self):
        return self.first_name


class Wishlist(models.Model):
    user_id = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey("product.Product", null=True, blank=True, on_delete=models.CASCADE)



