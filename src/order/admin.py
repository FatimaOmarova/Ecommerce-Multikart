from django.contrib import admin

from order import models


class CartModelAdmin(admin.ModelAdmin):
    list_display = ("product_id","user_id","count","total_price",)


# Register your models here.
admin.site.register(models.Cart, CartModelAdmin)