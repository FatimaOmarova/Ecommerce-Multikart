from django.contrib import admin
from product import models
from django.db.models import QuerySet
from typing import Any

from django.shortcuts import render
from .models import Image, Product
from modeltranslation.admin import TranslationAdmin

# cavid1
# cavid1234
# Register your models here.

class ColorModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name', ]

class SizeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)

class VendorModelAdmin(admin.ModelAdmin):
    list_display = ("name","image",)

class BrandModelAdmin(admin.ModelAdmin):
    list_display = ("name",)

class CategoryModelAdmin(TranslationAdmin):
    list_display = ("name",)
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ("name","rating",)


class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ("amount",)



class CategoryListFilter(admin.SimpleListFilter):
    title = "category"
    parameter_name = "category"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        names = model_admin.get_queryset(
            request=request
        ).values_list(
            "name", flat=True
        )
        lookups = []

        for name in names:
            lookups.append(
                (
                    name, f"Category name = {name}"
                )
            )

        return lookups

    def queryset(self, request: Any, queryset: QuerySet) -> QuerySet | None:
        value = self.value()
        if value:
            queryset = queryset.filter(name=value)
        return queryset




class ImageInline(admin.StackedInline):
    list_display = ("name",)
    model = Image
    # class  Meta:
    #     model = Image


    # def upload(request):
    #     if request.method == "POST":
    #         images = request.FILES.getlist('images')
    #         for image in images:
    #             Image.objects.create(images=image)





class ProductModelAdmin(TranslationAdmin):
    inlines = [ImageInline]
    exclude = [""]
    fieldsets = (
        (
            "Text Fields", {
                "fields": ("name", "description","febric","material","product_lenght")
            }
        ),
        (
            "Other", {
                "fields": ("price", "size", "created_at","color","avilablity","category","vendor","rating","status","brand","video","amount")}
        )
    )
    list_display = (
        "name",
        "price",
        "created_at",
        "category"
    )
    list_filter = ("created_at", "name", CategoryListFilter)
    readonly_fields = ("created_at",)
    search_fields = ['name','category','brand']
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



    # class Meta:
    #     model = Product


admin.site.register(models.Color , ColorModelAdmin)
admin.site.register(models.Size, SizeModelAdmin)
admin.site.register(models.Vendor, VendorModelAdmin)
admin.site.register(models.Category, CategoryModelAdmin)
admin.site.register(models.Review, ReviewModelAdmin)
admin.site.register(models.Brand, BrandModelAdmin)
admin.site.register(models.Image)
admin.site.register(models.Product, ProductModelAdmin)
admin.site.register(models.Discount, DiscountModelAdmin)