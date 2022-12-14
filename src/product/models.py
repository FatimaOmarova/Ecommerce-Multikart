from django.db import models
from colorfield.fields import ColorField
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class Color(models.Model):
    name = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

        
class Size(models.Model):
    name = models.CharField(
        max_length=128,
    )
    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(
        max_length=128,null=True, blank=True
    )
    image = models.ImageField(upload_to="uploads/vendor/% Y/% m/% d/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    followers = models.IntegerField(null=True, blank=True)
    review = models.IntegerField(null=True, blank=True)
    rating = models.FloatField()
    twitter = models.TextField(null=True, blank=True)
    gmail = models.TextField(null=True, blank=True)
    facebook = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,null=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=(Q(rating__gte=0) & Q(rating__lte=5)), name="rating0-5")
        ]

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=128,
    )
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=128,
    )
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(
        max_length=128,null=True,blank=True
    )
    price = models.FloatField(null=True,blank=True)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    avilablity = models.BooleanField(default=0,blank=True)
    category = models.ForeignKey("product.Category", null=True, blank=True, on_delete=models.CASCADE)
    vendor = models.ForeignKey("product.Vendor", null=True, blank=True, on_delete=models.CASCADE)
    rating = models.FloatField(default=0,blank=True)
    status = models.BooleanField(default=0,blank=True)
    description = models.TextField(null=True)
    febric = models.CharField(
        max_length=128,null=True,blank=True
    )
    brand = models.ForeignKey("product.Brand", null=True, blank=True, on_delete=models.CASCADE)
    material = models.CharField(
        max_length=128,null=True,blank=True
    )
    product_lenght = models.CharField(
        max_length=128,null=True,blank=True
    )
    video = models.TextField( null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True, null=True,blank=True
    )
    
    def images(self):
        return self.images_set.all()


    # def __str__(self):
    #     return self.name



class Image(models.Model):
    product =models.ForeignKey("product.Product",  related_name="images_set", null=True, blank=True, on_delete=models.CASCADE)
    name = models.ImageField(upload_to="product_image", null=True)
    is_main = models.BooleanField(default=False)


class Discount(models.Model):
    product = models.ForeignKey("product.Product", null=True, blank=True, on_delete=models.CASCADE) 
    amount = models.IntegerField()
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,null=True
    )
    def __str__(self):
        return self.name


class Review(models.Model):
    product =models.ForeignKey("product.Product", null=True, blank=True, on_delete=models.CASCADE)
    rating = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(5.0), 
            MinValueValidator(0)    
        ], null=True, blank=True
    )
    name = models.CharField(
        max_length=128,
    )
    email = models.CharField(
        max_length=250,
    )
    title = models.CharField(
        max_length=128,
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.name

