from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.cart),
    path('checkout',views.checkout),
    path('order-success', views.success),
    path('vendor-profile', views.vendor)
]