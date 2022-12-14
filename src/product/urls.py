from django.urls import path
from . import views

from .views import SearchResultsView

app_name = 'product'

urlpatterns = [
    path('category-page', views.category_page, name='category'),
    path('product-page/<int:pk>/',views.ProductDetailView.as_view(), name='product_details'),
    path('search', SearchResultsView.as_view(), name="search"),
    path('vendor-profile', views.vendor, name='vendor'),
    path("",views.ListProductAPIView.as_view(),name="product_list"),
    path("create/", views.CreateProductAPIView.as_view(),name="product_create"),
    path("update/<int:pk>/",views.UpdateProductAPIView.as_view(),name="update_product"),
    path("delete/<int:pk>/",views.DeleteProductAPIView.as_view(),name="delete_product")
    
]