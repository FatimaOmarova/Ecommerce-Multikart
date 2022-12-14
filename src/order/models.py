from django.db import models

# Create your models here.


class Cart(models.Model):
    product_id = models.ForeignKey("product.Product", null=True, blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey("users.User", null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )
    def __str__(self):
        return self.total_price
