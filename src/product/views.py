from django.shortcuts import render
from product.services.category_page import product_list, product_images,brand_list,new_products
from product.services.product import new_products, related_products
from django.db.models import Q
from .models import Product,Image,Brand
from product.forms import ProductReview
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import HttpResponseForbidden
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import ProductSerializer
from rest_framework import generics






def category_page(request):
    products = product_list()
    # images = all_product_images()
    images = product_list()
    brands = brand_list()
    new_product = new_products()
    for pro in new_product:
        print(pro.images)

    return render(request, 'product/category-page.html',context={"products": products,"images": images,"brands": brands,"new_products": new_product})

class ProductDetailView(FormMixin,DetailView):
    template_name='product/product-page.html'
    model = Product
    form_class = ProductReview
    
    def get_success_url(self):
        return reverse('product:product_details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)
    
        product = Product.objects.filter(id=self.kwargs.get('pk')).first()
        pictures = Image.objects.filter(product=self.kwargs.get('pk'))
        brands = Brand.objects.all()

        context_data["product"] = product
        context_data["pictures"] = pictures
        context_data["form"] =  ProductReview 
        context_data["brands"] = brands
        context_data["color"] = product.color.all()
        context_data["size"] = product.size.all()
        context_data["new_products"] = new_products()
        context_data["related_products"] = related_products(self.kwargs.get('pk'))
        return context_data
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)


    # def product_details(self,request, **kwargs ):
    #     product = Product.objects.get(id=self.kwargs.get('pk'))
    #     if request.method == "POST":
    #         form = ProductReview(request.POST)
    #         print(form)
    #         if form.is_valid():
    #             review = form.save(commit=False)
    #             review.product = product
    #             review.save()
    #     else:
    #         form = ProductReview()
        


# class ProductDetailView(FormMixin,DetailView):
#     template_name='product/product-page.html'
#     model = Product
#     form_class = 

#     def get_context_data(self, **kwargs) -> dict:
#         context_data = super().get_context_data(**kwargs)

#         product = Product.objects.filter(id=self.kwargs.get('pk')).first()
#         pictures = Image.objects.filter(product=self.kwargs.get('pk'))
#         brands = Brand.objects.all()

#         context_data["product"] = product
#         context_data["pictures"] = pictures
#         context_data["form"] =  ProductReview()
#         context_data["brands"] = brands
#         return context_data


class SearchResultsView(ListView):
    model = Product
    template_name = 'product/search.html'


    def get_queryset(self):
        query = self.request.GET.get("q") 
        print(query) 
        object_list = Product.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query) | Q(vendor__name__icontains=query))
        return object_list








def vendor(request):
    return render(request, 'product/vendor-profile.html')


class ListProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

