
from django.db.models import QuerySet, FilteredRelation, Q, F, OuterRef, Subquery
from django.contrib.postgres.aggregates import ArrayAgg


from product.models import Product,Image,Brand


def product_list() -> QuerySet:
    products = Product.objects.all().order_by("-created_at").prefetch_related("images_set").annotate(
        images=ArrayAgg(
            "images_set__name",
            distinct=True,
            filter=Q(images_set__is_main=True)
        )
    )
    # print(products.values())
    return products

def product_images(product_id):
    return  Image.objects.filter(product = product_id)

def all_product_images() -> QuerySet:
    products =Product.objects.all()
    # return Product.objects.

def brand_list():
    return Brand.objects.all()


def new_products() -> QuerySet:
   return Product.objects.all().order_by("-created_at")[:3].prefetch_related("images_set").annotate(
        images=ArrayAgg(
            "images_set__name",
            distinct=True,
            filter=Q(images_set__is_main=True)
        )
    )

