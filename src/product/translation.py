from .models import Product, Category
from modeltranslation.translator import TranslationOptions, register


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "description", "febric", "material", )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )

