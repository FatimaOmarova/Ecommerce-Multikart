from django.db.models import QuerySet
from django.db.models import Q


from product.models import Vendor,Product, Category, Review
from django.contrib.postgres.aggregates import ArrayAgg

def product_list() -> QuerySet:

    last_8_products = Product.objects.values("name").order_by("-id")[:8]
    return reversed(last_8_products)

def vendor_list() ->QuerySet:
    vendor_list = Vendor.objects.all()
    return vendor_list



def latest_3_list() -> QuerySet:

    latest_3_list = Product.objects.values("name").order_by("-id")[:3]
    return (latest_3_list)




def category_list(category_id) ->QuerySet:

    category_items = Product.objects.filter(category_id__pk=category_id)
    return (category_items)



def product_category(product_id) -> QuerySet:

    category_id = Product.objects.get(pk=product_id)
    product_category = Product.objects.filter(category_id = category_id.id )
    return product_category
    


def search_results(search_query) ->QuerySet:

    results = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query) | Q(material__icontains=search_query))
    return (results)



def product_sort() -> QuerySet:

    sorted_products = Product.objects.order_by('price', 'created-at')
    return(sorted_products)




def categories_products() -> QuerySet:

    categories_of_products = Product.objects.values('category')
    return (categories_of_products)



def reviews_product(product_id) ->QuerySet:

    reviews_of_product = Review.objects.filter(product_id = product_id.id )
    return(reviews_of_product)


def new_products() -> QuerySet:
   return Product.objects.all().order_by("-created_at")[:3].prefetch_related("images_set").annotate(
        images=ArrayAgg(
            "images_set__name",
            distinct=True,
            filter=Q(images_set__is_main=True)
        )
    )

def related_products(id) -> QuerySet:
    product=Product.objects.get(id=id)
    return Product.objects.filter(category=product.category).exclude(id=id)[:6].prefetch_related("images_set").annotate(
        images=ArrayAgg(
            "images_set__name",
            distinct=True,
            filter=Q(images_set__is_main=True)
        )
    )
